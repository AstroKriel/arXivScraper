## { MODULE

##
## === DEPENDENCIES
##

## stdlib
import sys

## third-party
import requests

## local
from arxivscraper.config_paths import directories
from arxivscraper.support import articles, file_io
from arxivscraper.support.articles import TaskStatus


def download_pdf(
    article: articles.Article,
) -> None:
    """Download the PDF for `article` and update its task status to `D` in the mdfile."""
    pdf_path = directories.pdfs_dir / f"{article.arxiv_id}.pdf"
    md_path = directories.md_files_dir / f"{article.arxiv_id}.md"
    try:
        print("Title:", article.title)
        response = requests.get(
            url=article.url_pdf,
            stream=True,
        )
        response.raise_for_status()
        with open(pdf_path, "wb") as file_pointer:
            for chunk in response.iter_content(chunk_size=8192):
                file_pointer.write(chunk)
        print(f"Downloaded: {pdf_path}\n")
    except requests.RequestException as error:
        print(f"Error downloading file: {error}")
    article.task_status = TaskStatus.PENDING
    with open(md_path, "w") as file_pointer:
        articles.write_article_to_file(file_pointer, article=article)


def download_pdfs(
    articles_list: list[articles.Article],
    *,
    verbose: bool = False,
) -> None:
    """Download PDFs for all articles whose task status is `d`."""
    num_articles = len(articles_list)
    for article_index, article in enumerate(articles_list):
        if verbose:
            print(f"({article_index+1}/{num_articles})")
        if article.task_status == TaskStatus.DOWNLOAD:
            download_pdf(article)
        elif verbose:
            print("Article does not need to be downloaded.\n")


def main() -> None:
    file_io.create_directory(directories.pdfs_dir)
    articles_list = articles.read_all_markdown_files()
    download_pdfs(
        articles_list,
        verbose=False,
    )


if __name__ == "__main__":
    main()
    sys.exit(0)

## } MODULE
