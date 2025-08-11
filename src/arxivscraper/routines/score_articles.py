## ###############################################################
## LOAD MODULES
## ###############################################################

import sys
import time
import json
from openai import OpenAI
from typing import Any, Dict, Optional
from arxivscraper.utils import ww_articles, ww_file_io
from arxivscraper.io_configs import directories, file_names


## ###############################################################
## REQUEST GPT TO SCORE ARTICLE
## ###############################################################

def load_api_key() -> Optional[str]:
  file_path = directories.search_configs / file_names.ai_api_key
  try:
    if not file_path.is_file():
      print(
        f"Error. Could not locate the API key file: {file_path}\n"
        f"Create this file and put your key in it."
      )
      return None
    for line in file_path.read_text(encoding="utf-8").splitlines():
      api_key = line.strip().strip("'").strip('"')
      if api_key: return api_key
  except Exception as e:
    print(f"Error. Unable to read the API key.\n{e}")
  return None

def build_ai_client(api_key: str) -> OpenAI:
  return OpenAI(api_key=api_key)

def get_ai_response(
    *,
    ai_client        : OpenAI,
    article_title    : str,
    article_abstract : str,
    prompt_rules     : str,
    prompt_criteria  : str,
    ai_model         : str = "gpt-4o-mini",
  ) -> Dict[str, Any]:
  if not article_title:
     return {
      "status"      : "error",
      "error"       : "missing article title",
      "ai_rating"   : None,
      "ai_reason"   : None,
      "ai_response" : None
    }
  if not article_abstract:
    return {
      "status"      : "error",
      "error"       : "missing article abstract",
      "ai_rating"   : None,
      "ai_reason"   : None,
      "ai_response" : None
    }
  prompt_input = f"{prompt_criteria}\n\nTITLE: {article_title}\n\nABSTRACT: {article_abstract}"
  try:
    ai_response = ai_client.chat.completions.create(
      model    = ai_model,
      messages = [
        { "role": "system", "content": prompt_rules },
        { "role": "user",   "content": prompt_input },
      ],
      temperature = 0.0
    )
  except Exception as e:
    return {
      "status"      : "error",
      "error"       : f"API call failed: {e}",
      "ai_rating"   : None,
      "ai_reason"   : None,
      "ai_response" : None
    }
  response_text = ""
  try:
    response_text = (ai_response.choices[0].message.content or "").strip()
    response_dict = json.loads(response_text)
    ai_rating = float(response_dict["rating"])
    ai_reason = float(response_dict["reason"])
    return {
      "status"      : "success",
      "ai_rating"   : ai_rating,
      "ai_reason"   : ai_reason,
      "ai_response" : response_text
    }
  except Exception as e:
    return {
      "status"      : "error",
      "error"       : f"JSON parsing failed: {e}",
      "ai_rating"   : None,
      "ai_reason"   : None,
      "ai_response" : response_text
    }


## ###############################################################
## FUNCTION TO INTERPRET AI RESPONSE
## ###############################################################

def get_ai_score(
    article         : Dict[str, Any],
    ai_client       : OpenAI,
    prompt_rules    : str,
    prompt_criteria : str,
  ) -> bool:
  time_start = time.time()
  response_dict = get_ai_response(
    ai_client        = ai_client,
    article_title    = article.get("title", ""),
    article_abstract = article.get("abstract", ""),
    prompt_rules     = prompt_rules,
    prompt_criteria  = prompt_criteria,
  )
  time_elapsed = time.time() - time_start
  if response_dict["status"] != "success":
    print("Error:", response_dict.get("error", "<unknown error>"))
    ai_response = response_dict.get("ai_response")
    if ai_response: print("Raw LLM response:", ai_response)
    return False
  article["ai_rating"] = response_dict["ai_rating"]
  article["ai_reason"] = response_dict["ai_reason"]
  print("arXiv-id:", article.get("arxiv_id","<unknown id>"))
  print("Title:", article.get("title","").strip())
  print("Rating:", response_dict["ai_rating"])
  print(f"Elapsed time: {time_elapsed:.2f} seconds.")
  return True


## ###############################################################
## ROUTINE MAIN
## ###############################################################

def main():
  api_key = load_api_key()
  if not api_key:
    raise RuntimeError(f"OpenAI API key not found. Add it to {directories.search_configs / file_names.ai_api_key}.")
  ai_client = build_ai_client(api_key)
  print("Reading in all articles...")
  articles = ww_articles.read_all_markdown_files()
  articles = [
    article
    for article in articles
    if article.get("ai_rating") is None
  ]
  num_articles = len(articles)
  print(f"Preparing to score {len(articles)} articles.")
  prompt_rules    = ww_file_io.read_text_file(directories.search_configs / file_names.ai_rules)
  prompt_criteria = ww_file_io.read_text_file(directories.search_configs / file_names.ai_criteria)
  for article_index, article in enumerate(articles):
    print(f"({article_index+1}/{num_articles})")
    is_scored = get_ai_score(
      article         = article,
      ai_client       = ai_client,
      prompt_rules    = prompt_rules,
      prompt_criteria = prompt_criteria,
    )
    if is_scored: ww_articles.save_article(article, force=True)
    print(" ")


## ###############################################################
## ROUTINE ENTRY POINT
## ###############################################################

if __name__ == "__main__":
  main()
  sys.exit(0)


## END OF ROUTINE