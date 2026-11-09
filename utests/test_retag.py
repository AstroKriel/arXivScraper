## { U-TEST

##
## === DEPENDENCIES
##

## stdlib
import datetime
import unittest

## local
from arxivscraper.support import articles
from arxivscraper.workflows import retag

##
## === HELPERS
##


def _make_article(
    *,
    abstract: str,
    config_tags: list[str],
) -> articles.Article:
    return articles.Article(
        title="a paper",
        arxiv_id="2310.17036",
        url_pdf="https://arxiv.org/pdf/2310.17036v1",
        authors=["A. Author"],
        abstract=abstract,
        date_published=datetime.date(2023, 10, 26),
        date_updated=datetime.date(2023, 10, 26),
        category_primary="astro-ph.GA",
        category_others=[],
        config_tags=config_tags,
    )


_CONFIGS = {
    "dynamo": {
        "keywords_to_include": ["dynamo"],
        "keywords_to_exclude": [],
    },
    "ism": {
        "keywords_to_include": ["interstellar"],
        "keywords_to_exclude": [],
    },
}

##
## === TEST SUITE
##


class TestRetagArticles_Tags(unittest.TestCase):

    def test_adds_a_matching_tag_and_removes_a_stale_one(
        self,
    ) -> None:
        article = _make_article(
            abstract="a turbulent dynamo",
            config_tags=["#ism"],
        )
        retagged_articles = retag.retag_articles(
            articles_list=[article],
            configs=_CONFIGS,
        )
        self.assertEqual(retagged_articles, [article])
        self.assertEqual(article.config_tags, ["#dynamo"])

    def test_keeps_a_tag_that_belongs_to_no_profile(
        self,
    ) -> None:
        article = _make_article(
            abstract="a turbulent dynamo",
            config_tags=["#hand-picked"],
        )
        retag.retag_articles(
            articles_list=[article],
            configs=_CONFIGS,
        )
        self.assertEqual(article.config_tags, ["#dynamo", "#hand-picked"])

    def test_leaves_an_article_with_the_right_tags_unchanged(
        self,
    ) -> None:
        article = _make_article(
            abstract="a turbulent dynamo",
            config_tags=["#dynamo"],
        )
        retagged_articles = retag.retag_articles(
            articles_list=[article],
            configs=_CONFIGS,
        )
        self.assertEqual(retagged_articles, [])


##
## === ENTRY POINT
##

if __name__ == "__main__":
    unittest.main()

## } U-TEST
