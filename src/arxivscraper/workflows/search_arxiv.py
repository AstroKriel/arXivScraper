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
import requests
import unidecode

## local
from arxivscraper.config_paths import directories
from arxivscraper.support import articles, dates, file_io, script_cli, search_criteria


## keep these near arxiv.py defaults to avoid brittle request behavior and to
## respect arXiv's requested pacing between API calls.
_ARXIV_PAGE_SIZE = 100
_ARXIV_DELAY_SECONDS = 3.0
_ARXIV_NUM_RETRIES = 3
_ARXIV_CONNECT_TIMEOUT_SECONDS = 10.0
_ARXIV_READ_TIMEOUT_SECONDS = 20.0


class TimeoutSession(requests.Session):
    """Requests session that applies a default timeout to every request."""

    def __init__(
        self,
        connect_timeout: float,
        read_timeout: float,
    ) -> None:
        super().__init__()
        self.timeout = (
            connect_timeout,
            read_timeout,
        )

    def request(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> requests.Response:
        kwargs.setdefault("timeout", self.timeout)
        return super().request(*args, **kwargs)


class TimeoutClient(arxiv.Client):
    """arXiv client with explicit request timeouts on its internal session."""

    def __init__(
        self,
        *,
        page_size: int,
        delay_seconds: float,
        num_retries: int,
        connect_timeout: float,
        read_timeout: float,
    ) -> None:
        super().__init__(
            page_size=page_size,
            delay_seconds=delay_seconds,
            num_retries=num_retries,
        )
        self._session = TimeoutSession(
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
        )


class SearchArxiv():
    """Orchestrate a keyword-filtered arXiv search across all categories in a config file."""

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
        self.articles: list[articles.Article] = []
        self.client: arxiv.Client | None = None
        self.existing_ids: set[str] = set()
        self.search_criteria_config: dict[str, Any] = {}

    def search(
        self,
    ) -> None:
        self._read_search_criteria()
        self._read_existing_ids()
        self.client = self._build_client()
        for search_category in self.search_criteria_config["categories"]:
            print(f"Searching: {search_category}")
            print(
                f"Date range: {dates.cast_date_to_string(self.lookback_date)} to {dates.cast_date_to_string(self.current_date)}",
            )
            print("Requesting results from arXiv...")
            num_articles_looked_at_in_category = 0
            num_interesting_articles_in_category = 0
            num_new_articles_in_category = 0
            try:
                assert self.client is not None
                for arxiv_article in self.client.results(self._create_search_query(category=search_category)):
                    self._display_progress(num_articles_looked_at_in_category=num_articles_looked_at_in_category)
                    num_articles_looked_at_in_category += 1
                    if self._is_before_date_range(arxiv_article=arxiv_article):
                        break
                    if not (self._is_within_date_range(arxiv_article=arxiv_article)):
                        continue
                    arxiv_id = str(arxiv_article.pdf_url).split("/")[-1].split("v")[0]
                    if self._is_duplicate(this_arxiv_id=arxiv_id):
                        continue
                    assessment = self._check_config_conditions(arxiv_article=arxiv_article)
                    if assessment.is_match:
                        num_interesting_articles_in_category += 1
                        if arxiv_id in self.existing_ids:
                            continue
                        config_results = {self.config_name: assessment.reasons}
                        article = articles.get_article_summary(
                            arxiv_article=arxiv_article,
                            config_results=config_results,
                        )
                        self.articles.append(article)
                        num_new_articles_in_category += 1
            except requests.exceptions.Timeout:
                print(f"\nTimed out while reading arXiv results for {search_category}; skipping category.\n")
                continue
            except requests.exceptions.RequestException as error:
                print(f"\nRequest failed for {search_category}: {error}; skipping category.\n")
                continue
            except arxiv.HTTPError as error:
                print(f"\nHTTP error for {search_category}: {error}; skipping category.\n")
                continue
            print(
                f"\nFound {num_interesting_articles_in_category} interesting articles "
                f"({num_new_articles_in_category} new to local database) "
                f"from the {num_articles_looked_at_in_category} looked at.\n",
            )

    def get_sorted_articles(
        self,
    ) -> list[articles.Article]:
        return sorted(
            self.articles,
            key=lambda article: article.date_updated,
            reverse=True,
        )

    def _read_search_criteria(
        self,
    ) -> None:
        self.search_criteria_config = search_criteria.read_search_criteria(
            directory=directories.search_configs_dir,
            config_name=self.config_name,
        )
        print("Searching for articles:")
        print("> from: {}".format(dates.cast_date_to_string(self.lookback_date)))
        print("> to:   {}".format(dates.cast_date_to_string(self.current_date)))
        print(" ")
        print(f"> using the `#{self.config_name}` config file")
        print(" ")
        search_criteria.print_search_criteria(self.search_criteria_config)

    def _read_existing_ids(
        self,
    ) -> None:
        if not directories.md_files_dir.exists():
            self.existing_ids = set()
            return
        self.existing_ids = {
            file_path.stem
            for file_path in directories.md_files_dir.glob("*.md")
        }

    def _build_client(
        self,
    ) -> arxiv.Client:
        return TimeoutClient(
            page_size=_ARXIV_PAGE_SIZE,
            delay_seconds=_ARXIV_DELAY_SECONDS,
            num_retries=_ARXIV_NUM_RETRIES,
            connect_timeout=_ARXIV_CONNECT_TIMEOUT_SECONDS,
            read_timeout=_ARXIV_READ_TIMEOUT_SECONDS,
        )

    def _create_search_query(
        self,
        *,
        category: str,
    ) -> arxiv.Search:
        date_range = self._get_submitted_date_range_query()
        return arxiv.Search(
            query=f"{category} AND {date_range}",
            max_results=10**4,
            sort_by=arxiv.SortCriterion.SubmittedDate,
        )

    def _get_submitted_date_range_query(
        self,
    ) -> str:
        start = self.lookback_date.strftime("%Y%m%d0000")
        end = self.current_date.strftime("%Y%m%d2359")
        return f"submittedDate:[{start} TO {end}]"

    def _is_within_date_range(
        self,
        *,
        arxiv_article: arxiv.Result,
    ) -> bool:
        article_date = arxiv_article.published.date()
        return (self.lookback_date.date() <= article_date) and (article_date <= self.current_date.date())

    def _is_before_date_range(
        self,
        *,
        arxiv_article: arxiv.Result,
    ) -> bool:
        """Return `True` once results have moved older than the lower date bound."""
        article_date = arxiv_article.published.date()
        return article_date < self.lookback_date.date()

    def _is_duplicate(
        self,
        *,
        this_arxiv_id: str,
    ) -> bool:
        return any([this_arxiv_id == article.arxiv_id for article in self.articles])

    def _check_config_conditions(
        self,
        *,
        arxiv_article: arxiv.Result,
    ) -> articles.MatchAssessment:
        if search_criteria.meets_search_criteria(
                phrase=arxiv_article.title.lower(),
                search_keywords=self.search_criteria_config["keywords_to_exclude"],
        ):
            return articles.MatchAssessment(
                reasons=articles.MatchReasons(
                    title_match=False,
                    abstract_match=False,
                    author_match=False,
                ),
            )
        is_title_matching = search_criteria.meets_search_criteria(
            phrase=arxiv_article.title.lower(),
            search_keywords=self.search_criteria_config["keywords_to_include"],
        )
        if search_criteria.meets_search_criteria(
                phrase=arxiv_article.summary.lower(),
                search_keywords=self.search_criteria_config["keywords_to_exclude"],
        ):
            return articles.MatchAssessment(
                reasons=articles.MatchReasons(
                    title_match=False,
                    abstract_match=False,
                    author_match=False,
                ),
            )
        is_abstract_matching = search_criteria.meets_search_criteria(
            phrase=arxiv_article.summary.lower(),
            search_keywords=self.search_criteria_config["keywords_to_include"],
        )
        author_last_names = [
            unidecode.unidecode(str(author).lower().split(" ")[-1]) for author in arxiv_article.authors
        ]
        is_authors_matching = any(
            author.lower() in author_last_names for author in self.search_criteria_config["authors"]
        )
        return articles.MatchAssessment(
            reasons=articles.MatchReasons(
                title_match=is_title_matching,
                abstract_match=is_abstract_matching,
                author_match=is_authors_matching,
            ),
        )

    def _display_progress(
        self,
        *,
        num_articles_looked_at_in_category: int,
    ) -> None:
        if num_articles_looked_at_in_category == 0:
            print("Progress:", end=" ")
        elif (num_articles_looked_at_in_category % 10) == 0:
            print("x", end="")
        elif (num_articles_looked_at_in_category % 50) == 0:
            print(" ", end="")


def main() -> None:
    user_inputs = script_cli.GetUserInputs(include_search=True)
    search_inputs = user_inputs.get_search_inputs()
    end_date = search_inputs["from_date"]
    if end_date is None:
        end_date = dates.get_date_today()
    arxiv_searcher = SearchArxiv(
        current_date=end_date,
        lookback_date=dates.get_date_n_days_before(
            end_date=end_date,
            day_count=search_inputs["lookback_days"],
        ),
        config_name=search_inputs["config_name"],
    )
    arxiv_searcher.search()
    articles_list = arxiv_searcher.get_sorted_articles()
    file_io.create_directory(directories.md_files_dir)
    for article in articles_list:
        articles.save_article(
            article=article,
            verbose=False,
            force=True,
        )
    print(f"Saved {len(articles_list)} articles.")
    print(" ")


if __name__ == "__main__":
    main()
    sys.exit(0)

## } MODULE
