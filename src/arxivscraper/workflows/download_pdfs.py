## { SCRIPT

##
## === DEPENDENCIES
##

## third-party
import requests

## personal
from huginn import manage_log, manage_shell

## local
from arxivscraper.config_paths import directories
from arxivscraper.support import articles, file_io

##
## === DOWNLOADING
## the browser downloads with these functions too, so they write nothing to the console.
##


def find_articles_to_download(
    articles_list: list[articles.Article],
) -> list[articles.Article]:
    return [_article for _article in articles_list if _article.task_status == articles.TaskStatus.DOWNLOAD]


def download_pdf(
    article: articles.Article,
) -> None:
    """Download the PDF of `article`, then set its status back to pending; raise `requests.RequestException` on failure.

    A failed download leaves the status as it was, so the paper stays marked for download.
    """
    file_io.create_directory(directories.get_pdfs_dir())
    pdf_path = directories.get_pdfs_dir() / f"{article.arxiv_id}.pdf"
    response = requests.get(
        url=article.url_pdf,
        stream=True,
        timeout=30,
    )
    response.raise_for_status()
    with open(pdf_path, "wb") as file_pointer:
        for chunk in response.iter_content(chunk_size=8192):
            file_pointer.write(chunk)
    article.task_status = articles.TaskStatus.PENDING
    articles.write_article_file(article)


##
## === COMMAND
##


def cmd_download() -> None:
    """Download the PDF of every paper marked for download."""
    manage_log.log_task("finding papers marked for download")
    articles_to_download = find_articles_to_download(articles.read_all_markdown_files())
    if not articles_to_download:
        manage_log.log_outcome(
            "no papers are marked for download",
            status=manage_log.OutcomeStatus.SKIPPED,
        )
        return
    manage_log.log_outcome(
        f"{len(articles_to_download)} papers to download",
        status=manage_log.OutcomeStatus.SUCCESS,
    )
    num_downloaded = 0
    for article in articles_to_download:
        manage_log.log_task(f"downloading {article.arxiv_id}")
        try:
            manage_shell.run_fn(
                description=f"download {article.arxiv_id}.pdf",
                fn=lambda: download_pdf(article),
            )
        except requests.RequestException as error:
            manage_log.log_outcome(
                "download failed; it stays marked for download",
                status=manage_log.OutcomeStatus.FAILURE,
                items={"error": str(error)},
            )
            continue
        num_downloaded += 1
        manage_log.log_outcome(
            f"downloaded to {directories.get_pdfs_dir()}",
            status=manage_log.OutcomeStatus.SUCCESS,
            items={"title": article.title},
        )
    if num_downloaded < len(articles_to_download):
        summary_status = manage_log.OutcomeStatus.WARNING
    else:
        summary_status = manage_log.OutcomeStatus.SUCCESS
    manage_log.log_outcome(
        f"downloaded {num_downloaded} of {len(articles_to_download)} papers",
        status=summary_status,
    )


## } SCRIPT
