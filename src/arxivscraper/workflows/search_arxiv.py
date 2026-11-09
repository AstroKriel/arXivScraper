## { SCRIPT

##
## === DEPENDENCIES
##

## stdlib
import datetime
from typing import Any

## third-party
import arxiv
import requests
import unidecode

## personal
from huginn import manage_log, manage_shell

## local
from arxivscraper.config_paths import directories
from arxivscraper.support import (
    articles,
    dates,
    file_io,
    input_value_types,
    search_criteria,
)

##
## === CONSTANTS
##

## keep these near arxiv.py defaults to avoid brittle request behavior and to
## respect arXiv's requested pacing between API calls.
_ARXIV_PAGE_SIZE = 100
_ARXIV_DELAY_SECONDS = 3.0
_ARXIV_NUM_RETRIES = 3
_ARXIV_CONNECT_TIMEOUT_SECONDS = 10.0
_ARXIV_READ_TIMEOUT_SECONDS = 20.0

##
## === TIMEOUT HELPERS
##


class _TimeoutSession(requests.Session):
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


class _TimeoutClient(arxiv.Client):
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
        self._session = _TimeoutSession(
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
        )


##
## === ARXIV SEARCH
##


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
        """Run the arXiv search across all configured categories and populate `self.articles`."""
        self._read_search_criteria()
        self._read_existing_ids()
        self.client = self._build_client()
        for search_category in self.search_criteria_config["categories"]:
            manage_log.log_task(f"searching {search_category}")
            num_articles_looked_at_in_category = 0
            num_interesting_articles_in_category = 0
            num_new_articles_in_category = 0
            try:
                if self.client is None:
                    raise RuntimeError("client was not initialised.")
                for arxiv_article in self.client.results(self._create_search_query(category=search_category)):
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
                manage_log.log_outcome(
                    f"timed out reading arXiv results, so skipped {search_category}",
                    status=manage_log.OutcomeStatus.WARNING,
                )
                continue
            except (requests.exceptions.RequestException, arxiv.HTTPError) as error:
                manage_log.log_outcome(
                    f"arXiv request failed, so skipped {search_category}",
                    status=manage_log.OutcomeStatus.WARNING,
                    items={"error": str(error)},
                )
                continue
            manage_log.log_outcome(
                f"{num_interesting_articles_in_category} matching papers, {num_new_articles_in_category} new",
                status=manage_log.OutcomeStatus.SUCCESS,
                items={"papers checked": num_articles_looked_at_in_category},
            )

    def get_sorted_articles(
        self,
    ) -> list[articles.Article]:
        """Return `self.articles` sorted by `date_updated` descending."""
        return sorted(
            self.articles,
            key=lambda article: article.date_updated,
            reverse=True,
        )

    def _read_search_criteria(
        self,
    ) -> None:
        manage_log.log_task(f"reading search profile `{self.config_name}`")
        self.search_criteria_config = search_criteria.read_search_criteria(
            directory=directories.get_search_configs_dir(),
            config_name=self.config_name,
        )
        search_items = {
            "from": dates.as_date_string(self.lookback_date),
            "to": dates.as_date_string(self.current_date),
        }
        search_items.update(search_criteria.describe_search_criteria(self.search_criteria_config))
        manage_log.log_outcome(
            f"searching papers updated in the last {(self.current_date - self.lookback_date).days} days",
            status=manage_log.OutcomeStatus.SUCCESS,
            items=search_items,
        )

    def _read_existing_ids(
        self,
    ) -> None:
        md_files_dir = directories.get_md_files_dir()
        if not md_files_dir.exists():
            self.existing_ids = set()
            return
        self.existing_ids = {_file_path.stem for _file_path in md_files_dir.glob("*.md")}

    def _build_client(
        self,
    ) -> arxiv.Client:
        return _TimeoutClient(
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
        date_range = self._get_updated_date_range_query()
        return arxiv.Search(
            query=f"{category} AND {date_range}",
            max_results=10**4,
            sort_by=arxiv.SortCriterion.LastUpdatedDate,
        )

    def _get_updated_date_range_query(
        self,
    ) -> str:
        start = self.lookback_date.strftime("%Y%m%d0000")
        end = self.current_date.strftime("%Y%m%d2359")
        return f"lastUpdatedDate:[{start} TO {end}]"

    def _is_within_date_range(
        self,
        *,
        arxiv_article: arxiv.Result,
    ) -> bool:
        article_date = arxiv_article.updated.date()
        return (self.lookback_date.date() <= article_date) and (article_date <= self.current_date.date())

    def _is_before_date_range(
        self,
        *,
        arxiv_article: arxiv.Result,
    ) -> bool:
        """Return `True` once results have moved older than the lower date bound."""
        article_date = arxiv_article.updated.date()
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
        if search_criteria.check_search_criteria(
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
        is_title_matching = search_criteria.check_search_criteria(
            phrase=arxiv_article.title.lower(),
            search_keywords=self.search_criteria_config["keywords_to_include"],
        )
        if search_criteria.check_search_criteria(
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
        is_abstract_matching = search_criteria.check_search_criteria(
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

##
## === COMMAND
##


def _save_articles(
    articles_list: list[articles.Article],
) -> None:
    file_io.create_directory(directories.get_md_files_dir())
    for article in articles_list:
        articles.save_article(article)


def cmd_search(
    *,
    profile_name: str | None,
    lookback_days: int | None,
    from_date: datetime.date | None,
) -> None:
    """Search arXiv with a search profile and save the new matching papers; asks for any argument left out."""
    if profile_name is None:
        profile_name = str(
            manage_log.ask(
                "which search profile?",
                input_value_type=input_value_types.InputValueTypes.PROFILE,
            ),
        )
    if lookback_days is None:
        lookback_days = int(
            manage_log.ask(
                "how many days back?",
                input_value_type=input_value_types.InputValueTypes.NUMBER,
            ),
        )
    if from_date is None:
        end_date = dates.get_date_today()
    else:
        end_date = dates.as_datetime(from_date)
    arxiv_searcher = SearchArxiv(
        current_date=end_date,
        lookback_date=dates.get_date_n_days_before(
            end_date=end_date,
            day_count=lookback_days,
        ),
        config_name=profile_name,
    )
    arxiv_searcher.search()
    new_articles = arxiv_searcher.get_sorted_articles()
    manage_log.log_task("saving the new papers")
    if not new_articles:
        manage_log.log_outcome(
            "no new papers to save",
            status=manage_log.OutcomeStatus.SKIPPED,
        )
        return
    manage_shell.run_fn(
        description=f"save {len(new_articles)} papers to {directories.get_md_files_dir()}",
        fn=lambda: _save_articles(new_articles),
    )
    manage_log.log_outcome(
        f"saved {len(new_articles)} new papers",
        status=manage_log.OutcomeStatus.SUCCESS,
    )

## } SCRIPT
