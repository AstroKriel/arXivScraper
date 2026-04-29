## { MODULE

##
## === DEPENDENCIES
##

## stdlib
import sys
import webbrowser

## third-party
from rich.markup import escape as rich_escape
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import DataTable, Footer, Header, Static

## local
from arxivscraper.io_configs import directories
from arxivscraper.routines import download_articles
from arxivscraper.utils import article_utils, io_utils
from arxivscraper.utils.article_utils import TaskStatus

##
## === CONSTANTS
##

_FILTER_CYCLE: list[TaskStatus | None] = [
    None,  # no filter; show all articles
    TaskStatus.PENDING,
    TaskStatus.QUEUED,
    TaskStatus.READ,
    TaskStatus.DOWNLOAD,
    TaskStatus.NA,
    TaskStatus.DELETE,
]

##
## === TUI APP
##


class BrowseApp(App[None]):
    """TUI browser for reviewing and triaging saved arXiv articles."""

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

    TITLE = "arXiv Browser"

    BINDINGS = [
        Binding(
            key=status.key,
            action=f"set_status('{status.value}')",
            description=status.description,
        )
        for status in TaskStatus
    ] + [
        Binding(
            key="D",
            action="apply_downloads",
            description="apply download",
        ),
        Binding(
            key="X",
            action="apply_deletions",
            description="apply delete",
        ),
        Binding(
            key="o",
            action="open_pdf",
            description="open PDF",
        ),
        Binding(
            key="f",
            action="cycle_filter",
            description="filter",
        ),
        Binding(
            key="escape",
            action="quit",
            description="quit",
        ),
    ]

    def __init__(
        self,
        articles: list[article_utils.Article],
    ) -> None:
        super().__init__()
        self.all_articles = articles
        self.filter_status: TaskStatus | None = None

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
        table.add_columns(
            "Status",
            "Tags",
            "Category",
            "Date",
            "ID",
            "Title",
        )
        self._refresh_table()

    def _get_visible_articles(
        self,
    ) -> list[article_utils.Article]:
        if self.filter_status is None:
            return self.all_articles
        return [article for article in self.all_articles if article.task_status == self.filter_status]

    def _refresh_table(
        self,
        *,
        keep_row: int = 0,
    ) -> None:
        table = self.query_one(DataTable)
        table.clear()
        articles = self._get_visible_articles()
        for article in articles:
            table.add_row(
                article.task_status.value,
                " ".join(article.config_tags),
                article.category_primary,
                str(article.date_updated),
                article.arxiv_id,
                article.title,
            )
        if articles:
            row = min(keep_row, len(articles) - 1)
            table.move_cursor(
                row=row,
                scroll=True,
            )
            self._update_abstract(row_index=row)
        else:
            self.query_one("#abstract", Static).update("[dim]No papers match this filter.[/dim]")
        self._update_subtitle()

    def _update_abstract(
        self,
        *,
        row_index: int,
    ) -> None:
        articles = self._get_visible_articles()
        if not articles:
            return
        article = articles[row_index]
        self.query_one("#abstract", Static).update(
            f"[bold]{rich_escape(article.title)}[/bold]\n"
            f"[dim]{rich_escape(', '.join(article.authors))}[/dim]\n\n"
            f"{rich_escape(article.abstract)}",
        )

    def _update_subtitle(
        self,
    ) -> None:
        articles = self._get_visible_articles()
        filter_label = "all" if self.filter_status is None else self.filter_status.value
        self.sub_title = f"filter: {filter_label}  ({len(articles)} papers)"

    def on_data_table_row_highlighted(
        self,
        event: DataTable.RowHighlighted,
    ) -> None:
        self._update_abstract(row_index=event.cursor_row)

    def _get_current_article(
        self,
    ) -> article_utils.Article | None:
        table = self.query_one(DataTable)
        articles = self._get_visible_articles()
        if not articles:
            return None
        return articles[table.cursor_row]

    def action_set_status(
        self,
        status: str,
    ) -> None:
        table = self.query_one(DataTable)
        current_row = table.cursor_row
        article = self._get_current_article()
        if article is None:
            return
        article.task_status = TaskStatus(status)
        file_path = directories.md_files_dir / f"{article.arxiv_id}.md"
        with open(file_path, "w") as file_pointer:
            article_utils.write_article_to_file(file_pointer, article=article)
        self._refresh_table(keep_row=current_row)

    def action_open_pdf(
        self,
    ) -> None:
        article = self._get_current_article()
        if article is None:
            return
        webbrowser.open(article.url_pdf)

    def action_apply_downloads(
        self,
    ) -> None:
        io_utils.create_directory(directories.pdfs_dir)
        download_articles.download_pdfs(self.all_articles)
        self._refresh_table()

    def action_apply_deletions(
        self,
    ) -> None:
        to_delete = [article for article in self.all_articles if article.task_status == TaskStatus.DELETE]
        for article in to_delete:
            (directories.md_files_dir / f"{article.arxiv_id}.md").unlink(missing_ok=True)
            self.all_articles.remove(article)
        self._refresh_table()

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
    articles = sorted(
        articles,
        key=lambda article: article.date_updated,
        reverse=True,
    )
    BrowseApp(articles).run()


##
## === ENTRY POINT
##

if __name__ == "__main__":
    main()
    sys.exit(0)

## } MODULE
