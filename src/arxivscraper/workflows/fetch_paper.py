## { SCRIPT

##
## === DEPENDENCIES
##

## third-party
import arxiv
import requests

## personal
from huginn import manage_log, manage_shell

## local
from arxivscraper.config_paths import directories
from arxivscraper.support import (
    articles,
    file_io,
    input_value_types,
)

##
## === PAPER FETCHING
##


def _fetch_arxiv_article(
    arxiv_id: str,
) -> arxiv.Result:
    """Return the arXiv result for `arxiv_id`; exit with an error if arXiv has no such paper or cannot be reached."""
    client = arxiv.Client()
    search = arxiv.Search(id_list=[arxiv_id])
    try:
        arxiv_article = next(client.results(search), None)
    except (requests.exceptions.RequestException, arxiv.HTTPError) as error:
        manage_log.exit_with_error(f"could not reach arXiv: {error}")
    if arxiv_article is None:
        manage_log.exit_with_error(f"no arXiv paper with id `{arxiv_id}`")
    return arxiv_article


def _save_fetched_article(
    article: articles.Article,
) -> None:
    file_io.create_directory(directories.get_md_files_dir())
    articles.save_article(article)


##
## === COMMAND
##


def cmd_fetch(
    *,
    arxiv_id: str | None,
) -> None:
    """Fetch one paper by its arXiv id, show it for confirmation, and save it with a tag; asks for the id if left out."""
    if arxiv_id is None:
        arxiv_id = str(
            manage_log.ask(
                "which arXiv id?",
                input_value_type=input_value_types.InputValueTypes.ARXIV_ID,
            ),
        )
    manage_log.log_task(f"fetching {arxiv_id} from arXiv")
    arxiv_article = _fetch_arxiv_article(arxiv_id)
    preview_article = articles.get_article_summary(arxiv_article)
    manage_log.log_outcome(
        "found the paper",
        status=manage_log.OutcomeStatus.SUCCESS,
        items=articles.describe_article(preview_article),
    )
    paper_is_intended = manage_log.ask(
        "is this the paper you meant?",
        input_value_type=input_value_types.InputValueTypes.YES_OR_NO,
    )
    if not paper_is_intended:
        manage_log.log_outcome(
            "did not save the paper",
            status=manage_log.OutcomeStatus.SKIPPED,
        )
        return
    file_path = articles.get_article_file_path(preview_article)
    if file_path.exists():
        save_is_repeated = manage_log.ask(
            f"already saved at {file_path}; save it again?",
            input_value_type=input_value_types.InputValueTypes.YES_OR_NO,
        )
        if not save_is_repeated:
            manage_log.log_outcome(
                "kept the saved copy",
                status=manage_log.OutcomeStatus.SKIPPED,
            )
            return
    tag = manage_log.ask(
        "which tag should it get?",
        input_value_type=input_value_types.InputValueTypes.TAG,
    )
    ## a manual fetch has no real search assessment, so tag it as a title-only hit.
    config_results = {
        tag: articles.MatchReasons(
            title_match=True,
            abstract_match=False,
            author_match=False,
        ),
    }
    article = articles.get_article_summary(
        arxiv_article=arxiv_article,
        config_results=config_results,
    )
    manage_shell.run_fn(
        description=f"save {arxiv_id}.md",
        fn=lambda: _save_fetched_article(article),
    )
    manage_log.log_outcome(
        f"saved {arxiv_id} with the tag #{tag}",
        status=manage_log.OutcomeStatus.SUCCESS,
    )


## } SCRIPT
