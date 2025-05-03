## ###############################################################
## LOAD MODULES
## ###############################################################
import sys
from arXivScraper.utils import ww_articles
import requests
from arXivScraper.config import directories
from arXivScraper.utils import ww_file_io


## ###############################################################
## DOWNLOAD ARXIV PDF
## ###############################################################
def download_pdf(article):
  arxiv_id      = article["arxiv_id"]
  file_path_pdf = f"{directories.pdfs}/{arxiv_id}.pdf"
  file_path_md  = f"{directories.mdfiles}/{arxiv_id}.md"
  try:
    print("Title:", article["title"])
    response = requests.get(article["url_pdf"], stream=True)
    response.raise_for_status()
    with open(file_path_pdf, "wb") as file:
      for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)
    print(f"Downloaded: {file_path_pdf}\n")
  except requests.RequestException as e: print(f"Error downloading file: {e}")
  ## update task status stored in the markdown file
  article["task_status"] = "D"
  with open(file_path_md, "w") as file_pointer:
    ww_articles.write_article_to_file(file_pointer, article)


## ###############################################################
## DOWNLOAD MARKDOWN FILES WITH DOWNLOAD STATUS
## ###############################################################
def download_pdfs(articles, verbose=False):
  num_articles = len(articles)
  for article_index, article in enumerate(articles):
    if verbose: print(f"({article_index+1}/{num_articles})")
    if article.get("task_status", None) == "d":
      download_pdf(article)
    elif verbose: print("Article does not need to be downloaded.\n")


## ###############################################################
## ROUTINE MAIN
## ###############################################################
def main():
  ww_file_io.init_directory(directories.pdfs)
  articles = ww_articles.read_all_markdown_files()
  download_pdfs(articles, verbose=False)


## ###############################################################
## ROUTINE ENTRY POINT
## ###############################################################
if __name__ == "__main__":
  main()
  sys.exit(0)


## END OF ROUTINE