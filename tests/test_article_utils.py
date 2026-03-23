## { MODULE

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

## local
from arxivscraper.utils.article_utils import Article, format_text, read_markdown_file, truncate_list, write_article_to_file

##
## === HELPERS
##


def make_article(
    **kwargs,
) -> Article:
    defaults = dict(
        title="Turbulent MHD in the galactic halo",
        arxiv_id="2310.17036",
        url_pdf="https://arxiv.org/pdf/2310.17036",
        authors=["Smith, J.", "Jones, A."],
        abstract="We study magnetic field amplification via turbulent dynamo action.",
        date_published=datetime.date(2023, 10, 26),
        date_updated=datetime.date(2023, 10, 27),
        category_primary="astro-ph.GA",
        category_others=["physics.plasm-ph"],
        config_tags=["#mhd"],
        task_status="u",
        ai_rating=None,
        ai_reason=None,
        config_reasons={"mhd": [True, False, True]},
    )
    defaults.update(kwargs)
    return Article(**defaults)


def roundtrip(
    article: Article,
) -> Article:
    """Write an Article to a string buffer and read it back."""
    buf = io.StringIO()
    write_article_to_file(
        file_pointer=buf,
        article=article,
    )
    md_text = buf.getvalue()
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".md",
        delete=False,
    ) as f:
        f.write(md_text)
        tmp_path = pathlib.Path(f.name)
    try:
        return read_markdown_file(tmp_path)
    finally:
        tmp_path.unlink()


##
## === UNIT TESTS
##


class TestFormatText(unittest.TestCase):

    def test_removes_hash(
        self,
    ):
        self.assertEqual(
            first=format_text("Hello #world"),
            second="Hello world",
        )

    def test_replaces_colon_with_ellipsis(
        self,
    ):
        self.assertEqual(
            first=format_text("title: subtitle"),
            second="title... subtitle",
        )

    def test_replaces_double_quote_with_backtick(
        self,
    ):
        self.assertEqual(
            first=format_text('say "hello"'),
            second="say `hello`",
        )

    def test_adds_spaces_around_latex(
        self,
    ):
        result = format_text("energy$E=mc^2$here")
        self.assertIn(
            member=" $E=mc^2$ ",
            container=result,
        )

    def test_collapses_extra_spaces(
        self,
    ):
        self.assertEqual(
            first=format_text("too   many   spaces"),
            second="too many spaces",
        )

    def test_strips_leading_trailing(
        self,
    ):
        self.assertEqual(
            first=format_text("  padded  "),
            second="padded",
        )


class TestTruncateList(unittest.TestCase):

    def test_short_list_unchanged(
        self,
    ):
        self.assertEqual(
            first=truncate_list(elems=["a", "b", "c"], max_elems=5),
            second=["a", "b", "c"],
        )

    def test_long_list_truncated(
        self,
    ):
        result = truncate_list(
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
        result = truncate_list(
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
        result = truncate_list(elems=[1, 2, 3])
        self.assertEqual(
            first=result,
            second=["1", "2", "3"],
        )


class TestRoundtrip(unittest.TestCase):
    """Checks that write_article_to_file + read_markdown_file is lossless."""

    def test_basic_fields_preserved(
        self,
    ):
        original = make_article()
        restored = roundtrip(original)
        self.assertEqual(first=restored.title, second=original.title)
        self.assertEqual(first=restored.arxiv_id, second=original.arxiv_id)
        self.assertEqual(first=restored.url_pdf, second=original.url_pdf)
        self.assertEqual(first=restored.authors, second=original.authors)
        self.assertEqual(first=restored.date_published, second=original.date_published)
        self.assertEqual(first=restored.date_updated, second=original.date_updated)
        self.assertEqual(first=restored.category_primary, second=original.category_primary)
        self.assertEqual(first=restored.category_others, second=original.category_others)

    def test_task_status_preserved(
        self,
    ):
        for status in ["u", "d", "D", "-"]:
            with self.subTest(status=status):
                original = make_article(task_status=status)
                restored = roundtrip(original)
                self.assertEqual(
                    first=restored.task_status,
                    second=status,
                )

    def test_config_tags_preserved(
        self,
    ):
        original = make_article(config_tags=["#mhd", "#hydro"])
        restored = roundtrip(original)
        self.assertEqual(
            first=set(restored.config_tags),
            second={"#mhd", "#hydro"},
        )

    def test_config_reasons_preserved(
        self,
    ):
        original = make_article(config_reasons={"mhd": [True, False, True]})
        restored = roundtrip(original)
        self.assertEqual(
            first=restored.config_reasons,
            second={"mhd": [True, False, True]},
        )

    def test_multiple_config_reasons_preserved(
        self,
    ):
        original = make_article(
            config_reasons={"mhd": [True, False, True], "hydro": [False, True, False]},
        )
        restored = roundtrip(original)
        self.assertEqual(
            first=restored.config_reasons,
            second={"mhd": [True, False, True], "hydro": [False, True, False]},
        )

    def test_ai_rating_preserved(
        self,
    ):
        original = make_article(
            ai_rating=7.5,
            ai_reason="Highly relevant to dynamo theory.",
        )
        restored = roundtrip(original)
        self.assertAlmostEqual(first=restored.ai_rating, second=7.5)
        self.assertEqual(
            first=restored.ai_reason,
            second="Highly relevant to dynamo theory.",
        )

    def test_no_ai_rating_stays_none(
        self,
    ):
        original = make_article(
            ai_rating=None,
            ai_reason=None,
        )
        restored = roundtrip(original)
        self.assertIsNone(restored.ai_rating)
        self.assertIsNone(restored.ai_reason)

    def test_empty_category_others(
        self,
    ):
        original = make_article(category_others=[])
        restored = roundtrip(original)
        self.assertEqual(
            first=restored.category_others,
            second=[],
        )

    def test_empty_config_tags(
        self,
    ):
        original = make_article(config_tags=[])
        restored = roundtrip(original)
        self.assertEqual(
            first=restored.config_tags,
            second=[],
        )


class TestMergeLogic(unittest.TestCase):
    """Tests the merge behaviour in save_article via direct attribute manipulation."""

    def test_config_tags_merge_deduplicates(
        self,
    ):
        existing = make_article(config_tags=["#mhd", "#hydro"])
        incoming = make_article(config_tags=["#mhd", "#dynamo"])
        ## simulate the merge logic from save_article
        incoming.config_tags = list(set(incoming.config_tags) | set(existing.config_tags))
        self.assertEqual(
            first=set(incoming.config_tags),
            second={"#mhd", "#hydro", "#dynamo"},
        )

    def test_ai_rating_retained_from_existing(
        self,
    ):
        existing = make_article(ai_rating=8.0, ai_reason="Very relevant.")
        incoming = make_article(ai_rating=None, ai_reason=None)
        ## simulate the merge logic from save_article
        if existing.ai_rating is not None and incoming.ai_rating is None:
            incoming.ai_rating = existing.ai_rating
        if existing.ai_reason is not None and incoming.ai_reason is None:
            incoming.ai_reason = existing.ai_reason
        self.assertAlmostEqual(first=incoming.ai_rating, second=8.0)
        self.assertEqual(
            first=incoming.ai_reason,
            second="Very relevant.",
        )

    def test_ai_rating_not_overwritten_if_already_set(
        self,
    ):
        existing = make_article(ai_rating=8.0)
        incoming = make_article(ai_rating=6.5)
        ## simulate the merge logic from save_article
        if existing.ai_rating is not None and incoming.ai_rating is None:
            incoming.ai_rating = existing.ai_rating
        self.assertAlmostEqual(first=incoming.ai_rating, second=6.5)

    def test_config_reasons_merged_without_overwriting(
        self,
    ):
        existing = make_article(
            config_reasons={"mhd": [True, False, True], "hydro": [False, True, False]},
        )
        incoming = make_article(config_reasons={"mhd": [False, True, False]})
        ## simulate the merge logic from save_article
        for config_name, reasons in existing.config_reasons.items():
            if config_name not in incoming.config_reasons:
                incoming.config_reasons[config_name] = reasons
        ## mhd should NOT be overwritten, hydro should be added
        self.assertEqual(
            first=incoming.config_reasons["mhd"],
            second=[False, True, False],
        )
        self.assertEqual(
            first=incoming.config_reasons["hydro"],
            second=[False, True, False],
        )

    def test_task_status_retained_from_existing(
        self,
    ):
        existing = make_article(task_status="D")
        incoming = make_article(task_status="u")
        ## simulate the merge logic from save_article
        incoming.task_status = existing.task_status
        self.assertEqual(
            first=incoming.task_status,
            second="D",
        )


##
## === ENTRY POINT
##

if __name__ == "__main__":
    unittest.main()
    sys.exit(0)

## } MODULE
