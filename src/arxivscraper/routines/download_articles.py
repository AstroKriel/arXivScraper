## ###############################################################
## LOAD MODULES
## ###############################################################

import sys
import requests
from arxivscraper.utils import article_utils, io_utils
from arxivscraper.io_configs import directories

## ###############################################################
## DOWNLOAD ARXIV PDF
## ###############################################################


def download_pdf(article):
    arxiv_id = article.get("arxiv_id")
    file_path_pdf = directories.output_pdfs / f"{arxiv_id}.pdf"
    file_path_md = directories.output_mdfiles / f"{arxiv_id}.md"
    try:
        print("Title:", article.get("title"))
        response = requests.get(article.get("url_pdf"), stream=True)
        response.raise_for_status()
        with open(file_path_pdf, "wb") as fp:
            for chunk in response.iter_content(chunk_size=8192):
                fp.write(chunk)
        print(f"Downloaded: {file_path_pdf}\n")
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")
    ## update task status stored in the markdown file
    article["task_status"] = "D"
    with open(file_path_md, "w") as file_pointer:
        article_utils.write_article_to_file(file_pointer, article)


## ###############################################################
## DOWNLOAD MARKDOWN FILES WITH DOWNLOAD STATUS
## ###############################################################


def download_pdfs(articles, verbose=False):
    num_articles = len(articles)
    for article_index, article in enumerate(articles):
        if verbose: print(f"({article_index+1}/{num_articles})")
        if article.get("task_status") == "d":
            download_pdf(article)
        elif verbose:
            print("Article does not need to be downloaded.\n")


## ###############################################################
## ROUTINE MAIN
## ###############################################################


def main():
    io_utils.init_directory(directories.output_pdfs)
    articles = article_utils.read_all_markdown_files()
    download_pdfs(articles, verbose=False)


## ###############################################################
## ROUTINE ENTRY POINT
## ###############################################################

if __name__ == "__main__":
    main()
    sys.exit(0)

## END OF ROUTINE
