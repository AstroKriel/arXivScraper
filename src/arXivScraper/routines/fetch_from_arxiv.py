## ###############################################################
## LOAD MODULES
## ###############################################################
import sys
import arxiv
from arXivScraper.utils import file_io, articles, user_inputs
from arXivScraper.config import directories


## ###############################################################
## FETCH ARTICLE FROM THE ARXIV
## ###############################################################
def fetch_from_arxiv(arxiv_id):
  client = arxiv.Client()
  search = arxiv.Search(id_list=[arxiv_id])
  dict_arxiv = next(client.results(search), None)
  if dict_arxiv is None:
    print(f"Error: the arXiv article `{arxiv_id}` does not exist.")
    return None
  _dict_article = articles.get_article_summary(dict_arxiv)
  print("The article you have requested:")
  articles.print_article(_dict_article)
  print(" ")
  input_right_article = input("Was this the article you intended to fetch? (y/n): ")
  print(" ")
  if input_right_article[0].lower() != "y": return None
  file_path_file = f"{directories.mdfiles}/{arxiv_id}.md"
  if file_io.file_exists(file_path_file):
    print(f"Note: this arXiv article has already been saved: {file_path_file}")
    input_save_again = input("Would you like to save it again? (y/n): ")
    print(" ")
    if input_save_again[0].lower() != "y": return _dict_article
  input_tag = input("Enter a config tag: ")
  print(" ")
  if input_tag == "": raise Exception("Error: config tag cannot be empty.")
  if " " in input_tag: raise Exception("Error: config tag cannot contain spaces.")
  dict_config_results = { input_tag : [ 1, 0, 0 ] }
  dict_article = articles.get_article_summary(
    dict_arxiv          = dict_arxiv,
    dict_config_results = dict_config_results
  )
  articles.save_article(dict_article)
  return dict_article


## ###############################################################
## MAIN PROGRAM
## ###############################################################
def main():
  obj_user_inputs = user_inputs.GetUserInputs()
  arxiv_id = obj_user_inputs.get_fetch_inputs()
  file_io.init_directory(directories.mdfiles, bool_add_space=True)
  fetch_from_arxiv(arxiv_id)


## ###############################################################
## PROGRAM ENTRY POINT
## ###############################################################
if __name__ == "__main__":
  main()
  sys.exit(0)


## END OF PROGRAM