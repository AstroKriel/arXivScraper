## { U-TEST

##
## === DEPENDENCIES
##

## stdlib
import datetime
import io
import pathlib
import sys
import tempfile
import unittest
from typing import Any

## local
from arxivscraper.support import articles

##
## === HELPERS
##


def _make_article(
    **kwargs: Any,
) -> articles.Article:
    defaults: dict[str, Any] = dict(
        title="sample title",
        arxiv_id="0000.00000",
        url_pdf="https://arxiv.org/pdf/0000.00000",
        authors=["Author A", "Author B"],
        abstract="sample abstract text.",
        date_published=datetime.date(2000, 1, 1),
        date_updated=datetime.date(2000, 1, 2),
        category_primary="cat.AA",
        category_others=["cat.BB"],
        config_tags=["#tag-a"],
        task_status=articles.TaskStatus.PENDING,
        ai_rating=None,
        ai_reason=None,
        config_reasons={
            "tag-a": articles.MatchReasons(
                title_match=True,
                abstract_match=False,
                author_match=True,
            ),
        },
    )
    defaults.update(kwargs)
    return articles.Article(**defaults)


def _roundtrip(
    *,
    article: articles.Article,
) -> articles.Article:
    """Write an Article to a string buffer and read it back."""
    buffer = io.StringIO()
    articles.write_article_to_file(
        buffer,
        article=article,
    )
    md_text = buffer.getvalue()
    with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".md",
            delete=False,
    ) as file_pointer:
        file_pointer.write(md_text)
        tmp_path = pathlib.Path(file_pointer.name)
    try:
        return articles.read_markdown_file(tmp_path)
    finally:
        tmp_path.unlink()


##
## === TEST SUITE
##


class TestFormatText_Cases(unittest.TestCase):

    def test_removes_hash(
        self,
    ):
        self.assertEqual(
            first=articles.format_text("word #tag word"),
            second="word tag word",
        )

    def test_replaces_colon_with_ellipsis(
        self,
    ):
        self.assertEqual(
            first=articles.format_text("prefix: suffix"),
            second="prefix... suffix",
        )

    def test_replaces_double_quote_with_backtick(
        self,
    ):
        self.assertEqual(
            first=articles.format_text('say "word"'),
            second="say `word`",
        )

    def test_adds_spaces_around_latex(
        self,
    ):
        result = articles.format_text("word$x=y^2$word")
        self.assertIn(
            member=" $x=y^2$ ",
            container=result,
        )

    def test_collapses_extra_spaces(
        self,
    ):
        self.assertEqual(
            first=articles.format_text("too   many   spaces"),
            second="too many spaces",
        )

    def test_strips_leading_trailing(
        self,
    ):
        self.assertEqual(
            first=articles.format_text("  padded  "),
            second="padded",
        )


class TestTruncateList_Cases(unittest.TestCase):

    def test_short_list_unchanged(
        self,
    ):
        self.assertEqual(
            first=articles.truncate_list(
                elems=["a", "b", "c"],
                max_elems=5,
            ),
            second=["a", "b", "c"],
        )

    def test_long_list_truncated(
        self,
    ):
        result = articles.truncate_list(
            elems=["a", "b", "c", "d", "e", "f"],
            max_elems=5,
        )
        self.assertEqual(
            first=result,
            second=["a", "b", "c", "d", "e", "..."],
        )

    def test_exact_length_not_truncated(
        self,
    ):
        result = articles.truncate_list(
            elems=["a", "b", "c"],
            max_elems=3,
        )
        self.assertEqual(
            first=result,
            second=["a", "b", "c"],
        )

    def test_elements_cast_to_string(
        self,
    ):
        result = articles.truncate_list(elems=[1, 2, 3])
        self.assertEqual(
            first=result,
            second=["1", "2", "3"],
        )


class TestArticle_Roundtrip(unittest.TestCase):
    """Checks that write_article_to_file + read_markdown_file is lossless."""

    def test_basic_fields_preserved(
        self,
    ):
        original = _make_article()
        restored = _roundtrip(article=original)
        self.assertEqual(
            first=restored.title,
            second=original.title,
        )
        self.assertEqual(
            first=restored.arxiv_id,
            second=original.arxiv_id,
        )
        self.assertEqual(
            first=restored.url_pdf,
            second=original.url_pdf,
        )
        self.assertEqual(
            first=restored.authors,
            second=original.authors,
        )
        self.assertEqual(
            first=restored.date_published,
            second=original.date_published,
        )
        self.assertEqual(
            first=restored.date_updated,
            second=original.date_updated,
        )
        self.assertEqual(
            first=restored.category_primary,
            second=original.category_primary,
        )
        self.assertEqual(
            first=restored.category_others,
            second=original.category_others,
        )

    def test_task_status_preserved(
        self,
    ):
        for status in [
            articles.TaskStatus.PENDING,
            articles.TaskStatus.QUEUED,
            articles.TaskStatus.READ,
            articles.TaskStatus.DOWNLOAD,
            articles.TaskStatus.NA,
            articles.TaskStatus.DELETE,
        ]:
            with self.subTest(status=status):
                original = _make_article(task_status=status)
                restored = _roundtrip(article=original)
                self.assertEqual(
                    first=restored.task_status,
                    second=status,
                )

    def test_config_tags_preserved(
        self,
    ):
        original = _make_article(config_tags=["#tag-a", "#tag-b"])
        restored = _roundtrip(article=original)
        self.assertEqual(
            first=set(restored.config_tags),
            second={"#tag-a", "#tag-b"},
        )

    def test_config_reasons_preserved(
        self,
    ):
        original = _make_article(
            config_reasons={
                "tag-a": articles.MatchReasons(
                    title_match=True,
                    abstract_match=False,
                    author_match=True,
                ),
            },
        )
        restored = _roundtrip(article=original)
        self.assertEqual(
            first=restored.config_reasons,
            second={
                "tag-a": articles.MatchReasons(
                    title_match=True,
                    abstract_match=False,
                    author_match=True,
                ),
            },
        )

    def test_multiple_config_reasons_preserved(
        self,
    ):
        original = _make_article(
            config_reasons={
                "tag-a": articles.MatchReasons(
                    title_match=True,
                    abstract_match=False,
                    author_match=True,
                ),
                "tag-b": articles.MatchReasons(
                    title_match=False,
                    abstract_match=True,
                    author_match=False,
                ),
            },
        )
        restored = _roundtrip(article=original)
        self.assertEqual(
            first=restored.config_reasons,
            second={
                "tag-a": articles.MatchReasons(
                    title_match=True,
                    abstract_match=False,
                    author_match=True,
                ),
                "tag-b": articles.MatchReasons(
                    title_match=False,
                    abstract_match=True,
                    author_match=False,
                ),
            },
        )

    def test_ai_rating_preserved(
        self,
    ):
        original = _make_article(
            ai_rating=7.5,
            ai_reason="sample ai reason.",
        )
        restored = _roundtrip(article=original)
        self.assertIsNotNone(restored.ai_rating)
        assert restored.ai_rating is not None
        self.assertAlmostEqual(
            first=restored.ai_rating,
            second=7.5,
        )
        self.assertEqual(
            first=restored.ai_reason,
            second="sample ai reason.",
        )

    def test_no_ai_rating_stays_none(
        self,
    ):
        original = _make_article(
            ai_rating=None,
            ai_reason=None,
        )
        restored = _roundtrip(article=original)
        self.assertIsNone(restored.ai_rating)
        self.assertIsNone(restored.ai_reason)

    def test_empty_category_others(
        self,
    ):
        original = _make_article(category_others=[])
        restored = _roundtrip(article=original)
        self.assertEqual(
            first=restored.category_others,
            second=[],
        )

    def test_empty_config_tags(
        self,
    ):
        original = _make_article(config_tags=[])
        restored = _roundtrip(article=original)
        self.assertEqual(
            first=restored.config_tags,
            second=[],
        )


class TestSaveArticle_MergeLogic(unittest.TestCase):
    """Tests the merge behaviour in save_article via direct attribute manipulation."""

    def test_config_tags_merge_deduplicates(
        self,
    ):
        existing = _make_article(config_tags=["#tag-a", "#tag-b"])
        incoming = _make_article(config_tags=["#tag-a", "#tag-c"])
        ## simulate the merge logic from save_article
        incoming.config_tags = list(set(incoming.config_tags) | set(existing.config_tags))
        self.assertEqual(
            first=set(incoming.config_tags),
            second={"#tag-a", "#tag-b", "#tag-c"},
        )

    def test_ai_rating_retained_from_existing(
        self,
    ):
        existing = _make_article(
            ai_rating=8.0,
            ai_reason="sample ai reason.",
        )
        incoming = _make_article(
            ai_rating=None,
            ai_reason=None,
        )
        ## simulate the merge logic from save_article
        if existing.ai_rating is not None and incoming.ai_rating is None:
            incoming.ai_rating = existing.ai_rating
        if existing.ai_reason is not None and incoming.ai_reason is None:
            incoming.ai_reason = existing.ai_reason
        self.assertIsNotNone(incoming.ai_rating)
        assert incoming.ai_rating is not None
        self.assertAlmostEqual(
            first=incoming.ai_rating,
            second=8.0,
        )
        self.assertEqual(
            first=incoming.ai_reason,
            second="sample ai reason.",
        )

    def test_ai_rating_not_overwritten_if_already_set(
        self,
    ):
        existing = _make_article(ai_rating=8.0)
        incoming = _make_article(ai_rating=6.5)
        ## simulate the merge logic from save_article
        if existing.ai_rating is not None and incoming.ai_rating is None:
            incoming.ai_rating = existing.ai_rating
        self.assertIsNotNone(incoming.ai_rating)
        assert incoming.ai_rating is not None
        self.assertAlmostEqual(
            first=incoming.ai_rating,
            second=6.5,
        )

    def test_config_reasons_merged_without_overwriting(
        self,
    ):
        existing = _make_article(
            config_reasons={
                "tag-a": articles.MatchReasons(
                    title_match=True,
                    abstract_match=False,
                    author_match=True,
                ),
                "tag-b": articles.MatchReasons(
                    title_match=False,
                    abstract_match=True,
                    author_match=False,
                ),
            },
        )
        incoming = _make_article(
            config_reasons={
                "tag-a": articles.MatchReasons(
                    title_match=False,
                    abstract_match=True,
                    author_match=False,
                ),
            },
        )
        ## simulate the merge logic from save_article
        for config_name, reasons in existing.config_reasons.items():
            if config_name not in incoming.config_reasons:
                incoming.config_reasons[config_name] = reasons
        ## tag-a should NOT be overwritten, tag-b should be added
        self.assertEqual(
            first=incoming.config_reasons["tag-a"],
            second=articles.MatchReasons(
                title_match=False,
                abstract_match=True,
                author_match=False,
            ),
        )
        self.assertEqual(
            first=incoming.config_reasons["tag-b"],
            second=articles.MatchReasons(
                title_match=False,
                abstract_match=True,
                author_match=False,
            ),
        )

    def test_task_status_retained_from_existing(
        self,
    ):
        existing = _make_article(task_status=articles.TaskStatus.DOWNLOAD)
        incoming = _make_article(task_status=articles.TaskStatus.PENDING)
        ## simulate the merge logic from save_article
        incoming.task_status = existing.task_status
        self.assertEqual(
            first=incoming.task_status,
            second=articles.TaskStatus.DOWNLOAD,
        )


##
## === ENTRY POINT
##

if __name__ == "__main__":
    unittest.main()
    sys.exit(0)

## } U-TEST
