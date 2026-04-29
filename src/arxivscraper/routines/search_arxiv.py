## { MODULE

##
## === DEPENDENCIES
##

## stdlib
import datetime
import sys
from typing import Any

## third-party
import arxiv
import unidecode

## local
from arxivscraper.io_configs import directories
from arxivscraper.utils import argparse_utils, article_utils, datetime_utils, filter_utils, io_utils

##
## === OPERATOR CLASS
##


class SearchArxiv():

    def __init__(
        self,
        *,
        lookback_date: datetime.datetime,
        current_date: datetime.datetime,
        config_name: str,
    ) -> None:
        self.lookback_date = lookback_date
        self.current_date = current_date
        self.config_name = config_name
        self.articles: list[article_utils.Article] = []
        self.client: arxiv.Client | None = None
        self.search_criteria: dict[str, Any] = {}

    def search(
        self,
    ) -> None:
        """Fetch and filter articles from arXiv for all categories in the config."""
        self._read_search_criteria()
        for search_category in self.search_criteria["categories"]:
            print(f"Searching: {search_category}")
            print(
                f"Date range: {datetime_utils.cast_date_to_string(self.lookback_date)} to {datetime_utils.cast_date_to_string(self.current_date)}",
            )
            self.client = arxiv.Client(
                page_size=200,
                delay_seconds=1,
                num_retries=100,
            )
            num_articles_looked_at_in_category = 0
            num_new_articles_saved_in_category = 0
            for arxiv_article in self.client.results(self._create_search_query(search_category)):
                self._display_progress(num_articles_looked_at_in_category)
                num_articles_looked_at_in_category += 1
                if not (self._is_within_date_range(arxiv_article)):
                    break
                arxiv_id = str(arxiv_article.pdf_url).split("/")[-1].split("v")[0]
                if self._is_duplicate(arxiv_id):
                    continue
                is_relevant, reasons = self._check_config_conditions(arxiv_article)
                if is_relevant:
                    config_results = {self.config_name: reasons}
                    article = article_utils.get_article_summary(
                        arxiv_article=arxiv_article,
                        config_results=config_results,
                    )
                    self.articles.append(article)
                    num_new_articles_saved_in_category += 1
            print(
                f"\nFound {num_new_articles_saved_in_category} interesting articles from the {num_articles_looked_at_in_category} looked at.\n",
            )

    def get_sorted_articles(
        self,
    ) -> list[article_utils.Article]:
        """Return all found articles sorted by update date, newest first."""
        return sorted(
            self.articles,
            key=lambda article: article.date_updated,
            reverse=True,
        )

    def _read_search_criteria(
        self,
    ) -> None:
        self.search_criteria = filter_utils.read_search_criteria(
            directory=directories.configs_dir,
            config_name=self.config_name,
        )
        print("Searching for articles:")
        print("> from: {}".format(datetime_utils.cast_date_to_string(self.lookback_date)))
        print("> to:   {}".format(datetime_utils.cast_date_to_string(self.current_date)))
        print(" ")
        print(f"> using the `#{self.config_name}` config file")
        print(" ")
        filter_utils.print_search_criteria(self.search_criteria)

    def _create_search_query(
        self,
        category: str,
    ) -> arxiv.Search:
        return arxiv.Search(
            query=category,
            max_results=10**4,
            sort_by=arxiv.SortCriterion.SubmittedDate,
        )

    def _is_within_date_range(
        self,
        arxiv_article: arxiv.Result,
    ) -> bool:
        article_date = arxiv_article.updated.date()
        return (self.lookback_date.date() <= article_date) and (article_date <= self.current_date.date())

    def _is_duplicate(
        self,
        this_arxiv_id: str,
    ) -> bool:
        return any([this_arxiv_id == article.arxiv_id for article in self.articles])

    def _check_config_conditions(
        self,
        arxiv_article: arxiv.Result,
    ) -> tuple[bool, list[bool]]:
        if filter_utils.meets_search_criteria(
                phrase=arxiv_article.title.lower(),
                search_keywords=self.search_criteria["keywords_to_exclude"],
        ):
            return False, []
        is_title_matching = filter_utils.meets_search_criteria(
            phrase=arxiv_article.title.lower(),
            search_keywords=self.search_criteria["keywords_to_include"],
        )
        if filter_utils.meets_search_criteria(
                phrase=arxiv_article.summary.lower(),
                search_keywords=self.search_criteria["keywords_to_exclude"],
        ):
            return False, []
        is_abstract_matching = filter_utils.meets_search_criteria(
            phrase=arxiv_article.summary.lower(),
            search_keywords=self.search_criteria["keywords_to_include"],
        )
        author_last_names = [
            unidecode.unidecode(str(author).lower().split(" ")[-1]) for author in arxiv_article.authors
        ]
        is_authors_matching = any(
            author.lower() in author_last_names for author in self.search_criteria["authors"]
        )
        reasons = [is_title_matching, is_abstract_matching, is_authors_matching]
        return any(reasons), reasons

    def _display_progress(
        self,
        num_articles_looked_at_in_category: int,
    ) -> None:
        if num_articles_looked_at_in_category == 0:
            print("Progress:", end=" ")
        elif (num_articles_looked_at_in_category % 10) == 0:
            print("x", end="")
        elif (num_articles_looked_at_in_category % 50) == 0:
            print(" ", end="")


##
## === MAIN
##


def main():
    user_inputs = argparse_utils.GetUserInputs(include_search=True)
    search_inputs = user_inputs.get_search_inputs()
    arxiv_searcher = SearchArxiv(
        current_date=datetime_utils.get_date_today(),
        lookback_date=datetime_utils.get_date_n_days_ago(search_inputs["lookback_days"]),
        config_name=search_inputs["config_name"],
    )
    arxiv_searcher.search()
    articles = arxiv_searcher.get_sorted_articles()
    io_utils.create_directory(directories.md_files_dir)
    for article in articles:
        article_utils.save_article(
            article=article,
            verbose=False,
            force=True,
        )
    print(f"Saved {len(articles)} articles.")
    print(" ")


##
## === ENTRY POINT
##

if __name__ == "__main__":
    main()
    sys.exit(0)

## } MODULE
