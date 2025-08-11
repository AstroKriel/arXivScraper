## ###############################################################
## LOAD MODULES
## ###############################################################

import sys
import arxiv
from arxivscraper.utils import ww_articles, ww_user_inputs, ww_file_io
from arxivscraper.io_configs import directories


## ###############################################################
## FETCH ARTICLE FROM THE ARXIV
## ###############################################################

def fetch_from_arxiv(arxiv_id):
  client = arxiv.Client()
  search = arxiv.Search(id_list=[arxiv_id])
  arxiv_article = next(client.results(search), None)
  if arxiv_article is None:
    print(f"Error: the arXiv article `{arxiv_id}` does not exist.")
    return None
  _article = ww_articles.get_article_summary(arxiv_article)
  print("The article you have requested:")
  ww_articles.print_article(_article)
  print(" ")
  user_confirmation = input("Was this the article you intended to fetch? (y/N): ").strip().lower()
  print(" ")
  if not user_confirmation.startswith("y"):
    return None
  file_path_file = directories.output_mdfiles / f"{arxiv_id}.md"
  if file_path_file.exists():
    print(f"Note: this arXiv article has already been saved: {file_path_file}")
    user_save_mdfile = input("Would you like to save it again? (y/N): ").strip().lower()
    print(" ")
    if not user_save_mdfile.startswith("y"):
      return _article
  user_tag = input("Enter a config tag: ").strip().lower()
  print(" ")
  if user_tag == "": raise Exception("Error: config tag cannot be empty.")
  if " " in user_tag: raise Exception("Error: config tag cannot contain spaces.")
  config_results = { user_tag : [ 1, 0, 0 ] }
  article = ww_articles.get_article_summary(
    arxiv_article          = arxiv_article,
    config_results = config_results
  )
  ww_articles.save_article(article)
  return article


## ###############################################################
## ROUTINE MAIN
## ###############################################################

def main():
  obj_user_inputs = ww_user_inputs.GetUserInputs(include_fetch=True)
  arxiv_id = obj_user_inputs.get_fetch_inputs()
  ww_file_io.init_directory(directories.output_mdfiles)
  fetch_from_arxiv(arxiv_id)


## ###############################################################
## ROUTINE ENTRY POINT
## ###############################################################

if __name__ == "__main__":
  main()
  sys.exit(0)


## END OF ROUTINE