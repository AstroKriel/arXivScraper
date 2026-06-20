## { SCRIPT

##
## === DEPENDENCIES
##

## stdlib
import sys

## third-party
import arxiv

## local
from arxivscraper.config_paths import directories
from arxivscraper.support import articles, file_io, script_cli

##
## === PAPER FETCHING
##


def fetch_from_arxiv(
    arxiv_id: str,
) -> articles.Article | None:
    """Fetch a single article by arXiv ID, confirm with the user, and save it on acceptance."""
    client = arxiv.Client()
    search = arxiv.Search(id_list=[arxiv_id])
    arxiv_article = next(client.results(search), None)
    if arxiv_article is None:
        print(f"Error: the arXiv article `{arxiv_id}` does not exist.")
        return None
    preview_article = articles.get_article_summary(arxiv_article)
    print("The article you have requested:")
    articles.print_article(preview_article)
    print(" ")
    user_confirmation = input("Was this the article you intended to fetch? (y/N): ").strip().lower()
    print(" ")
    if not user_confirmation.startswith("y"):
        return None
    file_path_file = directories.md_files_dir / f"{arxiv_id}.md"
    if file_path_file.exists():
        print(f"Note: this arXiv article has already been saved: {file_path_file}")
        user_save_mdfile = input("Would you like to save it again? (y/N): ").strip().lower()
        print(" ")
        if not user_save_mdfile.startswith("y"):
            return preview_article
    user_tag = input("Enter a config tag: ").strip().lower()
    print(" ")
    if user_tag == "":
        raise ValueError("`user_tag` must not be empty.")
    if " " in user_tag:
        raise ValueError(f"`user_tag` must not contain spaces; got `{user_tag}`.")
    ## a manual fetch has no real search assessment, so tag it as a title-only hit.
    config_results = {
        user_tag: articles.MatchReasons(
            title_match=True,
            abstract_match=False,
            author_match=False,
        ),
    }
    article = articles.get_article_summary(
        arxiv_article=arxiv_article,
        config_results=config_results,
    )
    articles.save_article(article)
    return article


##
## === PROGRAM MAIN
##


def main() -> None:
    user_inputs = script_cli.CLIParser(include_fetch=True)
    arxiv_id = user_inputs.get_fetch_inputs()
    file_io.create_directory(directories.md_files_dir)
    fetch_from_arxiv(arxiv_id)


##
## === ENTRY POINT
##

if __name__ == "__main__":
    main()
    sys.exit(0)

## } SCRIPT
