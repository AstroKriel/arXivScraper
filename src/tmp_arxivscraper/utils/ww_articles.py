## ###############################################################
## DEPENDANCIES
## ###############################################################

import os
import re
import yaml
import unidecode
from arxivscraper.utils import ww_dates, ww_file_io
from arxivscraper.config import directories


## ###############################################################
## HELPER FUNCTION
## ###############################################################

def truncate_list(elems, max_elems=5):
  truncated_elems = [
    str(elem)  if (elem_index <  max_elems+1)
    else "..." if (elem_index == max_elems+1)
    else None
    for elem_index, elem in enumerate(elems)
  ]
  return [
    elem
    for elem in truncated_elems
    if elem is not None
  ]

def format_text(text):
  ## adjust text for things that go wrong with Obsidian's tex-rendering
  text = text.replace("#", "")
  text = text.replace("\'", "")
  text = text.replace(":", "...")
  text = text.replace('"', "`")
  ## add spaces before and after text between two dollar signs (LaTeX math)
  text = re.sub(r"(\$.*?\$)", lambda m: f" {m.group(1)} ", text)
  ## remove any extra (eg, double) spaces that might have been added inadvertently
  text = re.sub(r"\s+", " ", text).strip()
  return text


## ###############################################################
## PRINT ARTICLE CONTENTS
## ###############################################################

def print_article(article, num_pad_chars=13):
  ## helper function
  def _print_line(category, content):
    if isinstance(content, list): content = ", ".join(content)
    category = f"{category}".ljust(num_pad_chars)
    print(f"{category}: {content}")
  ## print article information
  _print_line("Title",        article["title"])
  _print_line("PDF URL",      article["url_pdf"])
  _print_line("Date Updated", ww_dates.cast_date_to_string(article["date_updated"]))
  _print_line("Author(s)",    article["authors"])
  return


## ###############################################################
## SAVE FILE TO MARKDOWN
## ###############################################################

def write_article_to_file(file_pointer, article):
  ## helper functions
  def _format_list_if_defined(content):
    if not content: return None
    return content
  ## prepare the YAML frontmatter
  yaml_content = {
    "title":            format_text(article["title"]),
    "arxiv_id":         article["arxiv_id"],
    "url_pdf":          article["url_pdf"],
    "date_published":   ww_dates.cast_date_to_string(article["date_published"]),
    "date_updated":     ww_dates.cast_date_to_string(article["date_updated"]),
    "category_primary": article["category_primary"],
    "category_others":  _format_list_if_defined(article.get("category_others")),
    "config_tags":      _format_list_if_defined(article.get("config_tags")),
    "authors":          article.get("authors"),
    "abstract":         format_text(article["abstract"]),
  }
  ## optional keys handling (these can be lists, booleans, or strings)
  optional_key_conditions = [
    "config_reason_",
    "ai_rating",
    "ai_reason",
  ]
  ## dynamically add optional keys to YAML content
  for key, value in article.items():
    if any(
      key_condition in key
      for key_condition in optional_key_conditions
    ):
      yaml_content[key] = value
  ## Sort the YAML content alphabetically
  sorted_yaml_content = dict(sorted(yaml_content.items()))
  ## Dump the sorted YAML frontmatter to the file
  file_pointer.write("---\n")
  yaml.dump(sorted_yaml_content, file_pointer, default_flow_style=False, sort_keys=False)
  file_pointer.write("---\n")
  ## Write the task status
  task_status = article.get("task_status", "u")
  file_pointer.write(f" - [{task_status}] #task status\n")
  return

def save_article(article, verbose=True, force=False):
  file_name = article["arxiv_id"] + ".md"
  file_path_file = f"{directories.mdfiles}/{file_name}"
  if ww_file_io.file_exists(file_path_file):
    _article = read_markdown_file(file_path_file)
    _task_status = _article["task_status"]
    ## if the article has already been assessed, do not overwrite it
    if not(force) and _task_status in [ "D", "-" ]:
      if _task_status == "D": print("The following article has already been downloaded:")
      if _task_status == "-": print("The following article has already been ignored:")
      print_article(article)
      input_save = input("Do you want to save it again? (y/n): ")
      print(" ")
      if input_save[0].lower() != "y": return
    ## retain the task status
    article["task_status"] = _task_status
    ## merge `config_tags`: only add unique tags from `_article`
    if "config_tags" in _article:
      article["config_tags"] = list(
        set(article.get("config_tags", [])) | set(_article.get("config_tags", []))
      )
    ## retain `ai_rating` only if it is not None
    if _article.get("ai_rating") is not None:
      article["ai_rating"] = _article.get("ai_rating")
    ## retain `ai_reason` only if it is not None
    if _article.get("ai_reason") is not None:
      article["ai_reason"] = _article.get("ai_reason")
    ## merge `config_reason_*` keys from `_article` if they do not already exist in `article`
    for key, value in _article.items():
      if key.startswith("config_reason_") and key not in article:
        article[key] = value
  ## overwrite the file if it exists, but retain the Obsidian task status and search category tags
  with open(file_path_file, "w") as file_pointer:
    write_article_to_file(file_pointer, article)
  if verbose: print(f"Saved: {file_path_file}")
  return


## ###############################################################
## EXTRACT + COMBINE ARTICLE INFORMATION
## ###############################################################

def get_article_summary(arxiv_article, config_results={}, ai_results={}, task_status="u"):
  authors = [
    unidecode.unidecode(str(author))
    for author in truncate_list(arxiv_article.authors)
  ]
  other_categories = [
    format_text(elem)
    for elem in truncate_list(arxiv_article.categories)
    if (elem != arxiv_article.primary_category)
  ]
  config_tags = [
    f"#{key}" if ("#" not in key) else key
    for key in config_results.keys()
  ]
  article = {
    "title"               : format_text(arxiv_article.title),
    "arxiv_id"            : arxiv_article.pdf_url.split("/")[-1].split("v")[0],
    "url_pdf"             : arxiv_article.pdf_url,
    "authors"             : authors,
    "abstract"            : format_text(arxiv_article.summary),
    "date_published"      : arxiv_article.published.date(),
    "date_updated"        : arxiv_article.updated.date(),
    "category_primary"    : arxiv_article.primary_category,
    "category_others"     : other_categories,
    "config_tags"         : config_tags,
    "task_status"         : task_status,
  }
  for config_tag, reasons in config_results.items():
    article[f"config_reason_{config_tag}"] = reasons
  for ai_key, ai_value in ai_results.items():
    if   ai_key == "ai_rating": article["ai_rating"] = ai_value
    elif ai_key == "ai_reason": article["ai_reason"] = ai_value
  return article


## ###############################################################
## READ MARKDOWN (ARTICLE) FILES
## ###############################################################

def read_markdown_file(md_file):
  content = ww_file_io.read_markdown_file(md_file)
  ## split the file into frontmatter (YAML) and body (markdown)
  match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
  if match:
    front_matter = match.group(1)
    body = match.group(2)
  else: raise ValueError("Missing frontmatter section in the Markdown file.")
  ## parse the YAML frontmatter
  try:
    meta_data = yaml.safe_load(front_matter)
  except yaml.YAMLError as e: raise ValueError(f"Error parsing YAML frontmatter: {e}")
  ## ensure all required keys are present in the meta_data
  missing_keys = [
    key
    for key in [
      "title",
      "authors",
      "abstract",
      "arxiv_id",
      "url_pdf",
      "date_published",
      "date_updated",
      "category_primary",
      "category_others",
      "config_tags",
    ]
    if key not in meta_data
  ]
  if missing_keys: raise ValueError("Missing required keys in frontmatter:", ", ".join(missing_keys))
  ## extract all config_reason_* keys
  config_reasons = {
    key: value
    for key, value in meta_data.items()
    if key.startswith("config_reason_")
  }
  ## find the character inside the brackets [] on the same line as `#task`
  task_status = "u"
  task_match = re.search(r"^\s*-\s+\[([^\]]+)\].*#task", body, re.MULTILINE)
  if task_match: task_status = task_match.group(1)
  ## collect all the properties
  properties = {
    "title"            : meta_data.get("title"),
    "authors"          : meta_data.get("authors"),
    "abstract"         : meta_data.get("abstract"),
    "arxiv_id"         : meta_data.get("arxiv_id"),
    "url_pdf"          : meta_data.get("url_pdf"),
    "date_published"   : ww_dates.cast_string_to_date(meta_data.get("date_published")),
    "date_updated"     : ww_dates.cast_string_to_date(meta_data.get("date_updated")),
    "category_primary" : meta_data.get("category_primary"),
    "category_others"  : meta_data.get("category_others", None),
    "config_tags"      : meta_data.get("config_tags", []),
    "ai_rating"        : meta_data.get("ai_rating", None),
    "ai_reason"        : meta_data.get("ai_reason", None),
    "task_status"      : task_status,
    **config_reasons
  }
  return dict(sorted(properties.items()))

def read_all_markdown_files():
  file_names = [
    file_name
    for file_name in os.listdir(directories.mdfiles)
    if file_name.endswith(".md")
  ]
  articles = []
  for file_name in file_names:
    file_path_file = f"{directories.mdfiles}/{file_name}"
    article = read_markdown_file(file_path_file)
    articles.append(article)
  return articles


## END OF MODULE