## ###############################################################
## LOAD MODULES
## ###############################################################
import sys
import arxiv
from arXivScraper.utils import ww_articles, ww_user_inputs
from arXivScraper.utils import ww_file_io
from arXivScraper.config import directories


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
  input_right_article = input("Was this the article you intended to fetch? (y/n): ")
  print(" ")
  if input_right_article[0].lower() != "y": return None
  file_path_file = f"{directories.mdfiles}/{arxiv_id}.md"
  if ww_file_io.file_exists(file_path_file):
    print(f"Note: this arXiv article has already been saved: {file_path_file}")
    input_save_again = input("Would you like to save it again? (y/n): ")
    print(" ")
    if input_save_again[0].lower() != "y": return _article
  input_tag = input("Enter a config tag: ")
  print(" ")
  if input_tag == "": raise Exception("Error: config tag cannot be empty.")
  if " " in input_tag: raise Exception("Error: config tag cannot contain spaces.")
  config_results = { input_tag : [ 1, 0, 0 ] }
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
  obj_user_inputs = ww_user_inputs.GetUserInputs()
  arxiv_id = obj_user_inputs.get_fetch_inputs()
  ww_file_io.init_directory(directories.mdfiles)
  fetch_from_arxiv(arxiv_id)


## ###############################################################
## ROUTINE ENTRY POINT
## ###############################################################
if __name__ == "__main__":
  main()
  sys.exit(0)


## END OF ROUTINE