## { MODULE

##
## === DEPENDENCIES
##

## stdlib
import sys
import webbrowser

## third-party
from rich.markup import escape
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import DataTable, Footer, Header, Static

## local
from arxivscraper.io_configs import directories
from arxivscraper.utils import article_utils

##
## === CONSTANTS
##

_STATUS_LABELS = {
    "u": "unread",
    "r": "2read",
    "D": "done",
    "-":  "skip",
}

_FILTER_CYCLE = [None, "u", "r", "D", "-"]

##
## === TUI APP
##


class BrowseApp(App):

    CSS = """
    DataTable {
        height: 3fr;
    }
    #abstract {
        height: 2fr;
        border: solid $accent;
        padding: 1 2;
        overflow-y: auto;
    }
    """

    BINDINGS = [
        Binding("r",     "set_status('r')", "2read"),
        Binding("u",     "set_status('u')", "unread"),
        Binding("d",     "set_status('D')", "done"),
        Binding("i",     "set_status('-')", "skip"),
        Binding("o",     "open_pdf",        "open PDF"),
        Binding("f",     "cycle_filter",    "filter"),
        Binding("q",     "quit",            "quit"),
    ]

    TITLE = "arXiv Browser"

    def __init__(
        self,
        articles: list[article_utils.Article],
    ) -> None:
        super().__init__()
        self.all_articles = articles
        self.filter_status: str | None = None

    def compose(
        self,
    ) -> ComposeResult:
        yield Header()
        yield DataTable()
        yield Static(id="abstract")
        yield Footer()

    def on_mount(
        self,
    ) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.add_columns("St", "Date", "Category", "Tags", "Title")
        self._refresh_table()

    def _visible(
        self,
    ) -> list[article_utils.Article]:
        if self.filter_status is None:
            return self.all_articles
        return [a for a in self.all_articles if a.task_status == self.filter_status]

    def _refresh_table(
        self,
        keep_row: int = 0,
    ) -> None:
        table = self.query_one(DataTable)
        table.clear()
        articles = self._visible()
        for article in articles:
            table.add_row(
                article.task_status,
                str(article.date_updated),
                article.category_primary,
                " ".join(article.config_tags),
                article.title,
            )
        if articles:
            row = min(keep_row, len(articles) - 1)
            table.move_cursor(row=row, scroll=True)
            self._update_abstract(row)
        else:
            self.query_one("#abstract", Static).update("[dim]No papers match this filter.[/dim]")
        self._update_subtitle()

    def _update_abstract(
        self,
        row_index: int,
    ) -> None:
        articles = self._visible()
        if not articles:
            return
        article = articles[row_index]
        self.query_one("#abstract", Static).update(
            f"[bold]{escape(article.title)}[/bold]\n"
            f"[dim]{escape(', '.join(article.authors))}[/dim]\n\n"
            f"{escape(article.abstract)}"
        )

    def _update_subtitle(
        self,
    ) -> None:
        articles = self._visible()
        filter_label = "all" if self.filter_status is None else _STATUS_LABELS.get(self.filter_status, self.filter_status)
        self.sub_title = f"filter: {filter_label}  ({len(articles)} papers)"

    def on_data_table_row_highlighted(
        self,
        event: DataTable.RowHighlighted,
    ) -> None:
        self._update_abstract(event.cursor_row)

    def _current_article(
        self,
    ) -> article_utils.Article | None:
        table = self.query_one(DataTable)
        articles = self._visible()
        if not articles:
            return None
        return articles[table.cursor_row]

    def action_set_status(
        self,
        status: str,
    ) -> None:
        table = self.query_one(DataTable)
        current_row = table.cursor_row
        article = self._current_article()
        if article is None:
            return
        article.task_status = status
        file_path = directories.output_mdfiles / f"{article.arxiv_id}.md"
        with open(file_path, "w") as fp:
            article_utils.write_article_to_file(fp, article)
        self._refresh_table(keep_row=current_row)

    def action_open_pdf(
        self,
    ) -> None:
        article = self._current_article()
        if article is None:
            return
        webbrowser.open(article.url_pdf)

    def action_cycle_filter(
        self,
    ) -> None:
        current_index = _FILTER_CYCLE.index(self.filter_status)
        self.filter_status = _FILTER_CYCLE[(current_index + 1) % len(_FILTER_CYCLE)]
        self._refresh_table()


##
## === MAIN
##


def main() -> None:
    articles = article_utils.read_all_markdown_files()
    articles = sorted(articles, key=lambda a: a.date_updated, reverse=True)
    BrowseApp(articles).run()


##
## === ENTRY POINT
##

if __name__ == "__main__":
    main()
    sys.exit(0)

## } MODULE
