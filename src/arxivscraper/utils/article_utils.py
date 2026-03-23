## { MODULE

##
## === DEPENDENCIES
##

## stdlib
import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from collections.abc import Mapping
from typing import Any, Optional, TextIO

## third-party
import arxiv
import unidecode
import yaml

## local
from arxivscraper.io_configs import directories
from arxivscraper.utils import datetime_utils, io_utils

##
## === ARTICLE DATACLASS
##


@dataclass
class Article:
    title: str
    arxiv_id: str
    url_pdf: str
    authors: list[str]
    abstract: str
    date_published: date
    date_updated: date
    category_primary: str
    category_others: list[str]
    config_tags: list[str] = field(default_factory=list)
    task_status: str = "u"
    ai_rating: Optional[float] = None
    ai_reason: Optional[str] = None
    ## keyed by config name (without the "config_reason_" prefix)
    config_reasons: dict[str, list] = field(default_factory=dict)


##
## === HELPERS
##


def truncate_list(
    elems: list,
    max_elems: int = 5,
) -> list[str]:
    truncated_elems = []
    for elem_index, elem in enumerate(elems):
        if elem_index < max_elems:
            truncated_elems.append(str(elem))
        else:
            truncated_elems.append("...")
            break
    return truncated_elems


def format_text(
    text: str,
) -> str:
    ## adjust text for things that go wrong with Obsidian's tex-rendering
    text = text.replace("#", "")
    text = text.replace("\'", "")
    text = text.replace(":", "...")
    text = text.replace('"', "`")
    ## add spaces before and after text between two dollar signs (LaTeX math)
    text = re.sub(
        pattern=r"(\$.*?\$)",
        repl=lambda m: f" {m.group(1)} ",
        string=text,
    )
    ## remove any extra (eg, double) spaces that might have been added inadvertently
    text = re.sub(
        pattern=r"\s+",
        repl=" ",
        string=text,
    ).strip()
    return text


##
## === PRINT ARTICLE
##


def print_article(
    article: Article,
    *,
    num_pad_chars: int = 13,
) -> None:
    ## helper function
    def _print_line(
        category: str,
        content: str | list,
    ) -> None:
        if isinstance(content, list): content = ", ".join(content)
        category = f"{category}".ljust(num_pad_chars)
        print(f"{category}: {content}")

    ## print article information
    _print_line(
        category="Title",
        content=article.title,
    )
    _print_line(
        category="PDF URL",
        content=article.url_pdf,
    )
    _print_line(
        category="Date Updated",
        content=datetime_utils.cast_date_to_string(article.date_updated),
    )
    _print_line(
        category="Author(s)",
        content=article.authors,
    )


##
## === WRITE ARTICLE TO FILE
##


def write_article_to_file(
    file_pointer: TextIO,
    article: Article,
) -> None:
    ## prepare the YAML frontmatter
    yaml_content = {
        "title": article.title,
        "arxiv_id": article.arxiv_id,
        "url_pdf": article.url_pdf,
        "date_published": datetime_utils.cast_date_to_string(article.date_published),
        "date_updated": datetime_utils.cast_date_to_string(article.date_updated),
        "category_primary": article.category_primary,
        "category_others": article.category_others or None,
        "config_tags": article.config_tags or None,
        "authors": article.authors,
        "abstract": article.abstract,
    }
    ## add optional fields
    if article.ai_rating is not None:
        yaml_content["ai_rating"] = article.ai_rating
    if article.ai_reason is not None:
        yaml_content["ai_reason"] = article.ai_reason
    ## expand config_reasons back to flat config_reason_{name} keys
    for config_name, reasons in article.config_reasons.items():
        yaml_content[f"config_reason_{config_name}"] = reasons
    ## sort the yaml content alphabetically
    sorted_yaml_content = dict(sorted(yaml_content.items()))
    ## dump the sorted YAML frontmatter to the file
    file_pointer.write("---\n")
    yaml.dump(
        data=sorted_yaml_content,
        stream=file_pointer,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
    )
    file_pointer.write("---\n")
    ## write the task status
    file_pointer.write(f" - [{article.task_status}] #task status\n")


def save_article(
    article: Article,
    *,
    verbose: bool = True,
    force: bool = False,
) -> None:
    file_name = article.arxiv_id + ".md"
    file_path = directories.output_mdfiles / file_name
    if file_path.exists():
        existing_article = read_markdown_file(file_path)
        ## if the article has already been assessed, do not overwrite it
        if not (force) and existing_article.task_status in ["D", "-"]:
            if existing_article.task_status == "D": print("The following article has already been downloaded:")
            if existing_article.task_status == "-": print("The following article has already been ignored:")
            print_article(article)
            user_input = input("Do you want to save it again? (y/N): ").strip().lower()
            print(" ")
            if not user_input.startswith("y"):
                return
        ## retain the task status
        article.task_status = existing_article.task_status
        ## merge `config_tags`: only add unique tags
        article.config_tags = list(set(article.config_tags) | set(existing_article.config_tags))
        ## retain `ai_rating` and `ai_reason` only if not already set
        if existing_article.ai_rating is not None and article.ai_rating is None:
            article.ai_rating = existing_article.ai_rating
        if existing_article.ai_reason is not None and article.ai_reason is None:
            article.ai_reason = existing_article.ai_reason
        ## merge `config_reasons` from existing if not already present
        for config_name, reasons in existing_article.config_reasons.items():
            if config_name not in article.config_reasons:
                article.config_reasons[config_name] = reasons
    ## overwrite the file, retaining merged state
    with open(file_path, "w") as file_pointer:
        write_article_to_file(file_pointer, article)
    if verbose: print(f"Saved: {file_path}")


##
## === BUILD ARTICLE FROM ARXIV RESULT
##


def get_article_summary(
    arxiv_article: arxiv.Result,
    *,
    config_results: Mapping[str, list] | None = None,
    ai_results: dict[str, Any] | None = None,
    task_status: str = "u",
) -> Article:
    if config_results is None: config_results = {}
    if ai_results is None: ai_results = {}
    authors = [unidecode.unidecode(str(author)) for author in truncate_list(arxiv_article.authors)]
    other_categories = [
        format_text(elem)
        for elem in truncate_list(arxiv_article.categories)
        if (elem != arxiv_article.primary_category)
    ]
    config_tags = [f"#{key}" if ("#" not in key) else key for key in config_results.keys()]
    config_reasons = {key: reasons for key, reasons in config_results.items()}
    return Article(
        title=format_text(arxiv_article.title),
        arxiv_id=arxiv_article.pdf_url.split("/")[-1].split("v")[0],
        url_pdf=arxiv_article.pdf_url,
        authors=authors,
        abstract=format_text(arxiv_article.summary),
        date_published=arxiv_article.published.date(),
        date_updated=arxiv_article.updated.date(),
        category_primary=arxiv_article.primary_category,
        category_others=other_categories,
        config_tags=config_tags,
        task_status=task_status,
        ai_rating=ai_results.get("ai_rating"),
        ai_reason=ai_results.get("ai_reason"),
        config_reasons=config_reasons,
    )


##
## === READ MARKDOWN FILES
##


def read_markdown_file(
    file_path: Path,
) -> Article:
    content = io_utils.read_markdown_file(file_path)
    ## split the file into frontmatter (YAML) and body (markdown)
    match = re.match(
        pattern=r"^---\n(.*?)\n---\n(.*)",
        string=content,
        flags=re.DOTALL,
    )
    if match:
        front_matter = match.group(1)
        body = match.group(2)
    else:
        raise ValueError("Missing frontmatter section in the Markdown file.")
    ## parse the YAML frontmatter
    try:
        meta_data = yaml.safe_load(front_matter)
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML frontmatter: {e}")
    ## ensure all required keys are present in the meta_data
    missing_keys = [
        key for key in [
            "title",
            "authors",
            "abstract",
            "arxiv_id",
            "url_pdf",
            "date_published",
            "date_updated",
            "category_primary",
            "category_others",
            "config_tags",
        ] if key not in meta_data
    ]
    if missing_keys: raise ValueError("Missing required keys in frontmatter:", ", ".join(missing_keys))
    ## collect config_reason_* keys into a dict keyed by config name
    config_reasons = {
        key[len("config_reason_"):]: value
        for key, value in meta_data.items()
        if key.startswith("config_reason_")
    }
    ## find the character inside the brackets [] on the same line as `#task`
    task_status = "u"
    task_match = re.search(
        pattern=r"^\s*-\s+\[([^\]]+)\].*#task",
        string=body,
        flags=re.MULTILINE,
    )
    if task_match: task_status = task_match.group(1)
    return Article(
        title=meta_data.get("title"),
        authors=meta_data.get("authors"),
        abstract=meta_data.get("abstract"),
        arxiv_id=meta_data.get("arxiv_id"),
        url_pdf=meta_data.get("url_pdf"),
        date_published=datetime_utils.cast_string_to_date(meta_data.get("date_published")),
        date_updated=datetime_utils.cast_string_to_date(meta_data.get("date_updated")),
        category_primary=meta_data.get("category_primary"),
        category_others=meta_data.get("category_others") or [],
        config_tags=meta_data.get("config_tags") or [],
        ai_rating=meta_data.get("ai_rating"),
        ai_reason=meta_data.get("ai_reason"),
        task_status=task_status,
        config_reasons=config_reasons,
    )


def read_all_markdown_files() -> list[Article]:
    return [read_markdown_file(file_path) for file_path in sorted(directories.output_mdfiles.glob("*.md"))]

## } MODULE
