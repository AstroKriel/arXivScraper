## ###############################################################
## LOAD MODULES
## ###############################################################
import sys
import requests
from arXivScraper.config import directories
from arXivScraper.utils import articles, file_io


## ###############################################################
## DOWNLOAD ARXIV PDF
## ###############################################################
def download_pdf(dict_article):
  arxiv_id     = dict_article["arxiv_id"]
  file_path_pdf = f"{directories.pdfs}/{arxiv_id}.pdf"
  file_path_md  = f"{directories.mdfiles}/{arxiv_id}.md"
  ## download arxiv-pdf
  try:
    print("Title:", dict_article["title"])
    response = requests.get(dict_article["url_pdf"], stream=True)
    response.raise_for_status()
    with open(file_path_pdf, "wb") as file:
      for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)
    print(f"Downloaded: {file_path_pdf}\n")
  except requests.RequestException as e: print(f"Error downloading file: {e}")
  ## update task status stored in the markdown file
  dict_article["task_status"] = "D"
  with open(file_path_md, "w") as filepointer:
    articles.write_article_to_file(filepointer, dict_article)


## ###############################################################
## DOWNLOAD MARKDOWN FILES WITH DOWNLOAD STATUS
## ###############################################################
def download_pdfs(list_article_dicts, verbose=False):
  num_articles = len(list_article_dicts)
  for article_index, dict_article in enumerate(list_article_dicts):
    if verbose: print(f"({article_index+1}/{num_articles})")
    if dict_article.get("task_status", None) == "d":
      download_pdf(dict_article)
    elif verbose: print("Article does not need to be downloaded.\n")


## ###############################################################
## MAIN PROGRAM
## ###############################################################
def main():
  file_io.init_directory(directories.pdfs, bool_add_space=True)
  list_article_dicts = articles.read_all_markdown_files()
  download_pdfs(list_article_dicts, verbose=False)


## ###############################################################
## PROGRAM ENTRY POINT
## ###############################################################
if __name__ == "__main__":
  main()
  sys.exit(0)


## END OF PROGRAM