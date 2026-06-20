## { MODULE

##
## === DEPENDENCIES
##

## stdlib
from pathlib import Path
from typing import Any

## local
from arxivscraper.support import file_io

##
## === READ SEARCH CRITERIA
##


def _ensure_required_keys(
    *,
    config_criteria: dict[str, Any],
    config_name: str,
    required_keys: set[str],
) -> None:
    missing_keys = required_keys - config_criteria.keys()
    if len(missing_keys) > 0:
        raise ValueError(
            f"config file `{config_name}.toml` is missing required keys: {', '.join(sorted(missing_keys))}.",
        )


def read_search_criteria(
    *,
    directory: Path,
    config_name: str,
) -> dict[str, Any]:
    """Load and validate the TOML search config named `config_name` from `directory`."""
    required_keys = {
        "authors",
        "categories",
        "keywords_to_exclude",
        "keywords_to_include",
    }
    config_path = directory / f"{config_name}.toml"
    config_criteria = file_io.read_file(
        config_path,
        expected_extension=".toml",
    )
    _ensure_required_keys(
        config_criteria=config_criteria,
        config_name=config_name,
        required_keys=required_keys,
    )
    return config_criteria


##
## === KEYWORD MATCHING
##


def check_all_keywords_in_text(
    phrase: str,
    *,
    search_keywords: list[Any],
) -> bool:
    """Return `True` if `phrase` contains all keywords in `search_keywords`."""
    if len(search_keywords) == 0:
        return False
    results = []
    for keyword in search_keywords:
        if isinstance(keyword, str):
            result = keyword.lower() in phrase
            results.append(result)
        elif isinstance(keyword, list):
            result = check_any_keywords_in_text(
                phrase=phrase,
                search_keywords=keyword,
            )
            results.append(result)
    return all(results)


def check_any_keywords_in_text(
    phrase: str,
    *,
    search_keywords: list[Any],
) -> bool:
    """Return `True` if `phrase` contains at least one keyword in `search_keywords`."""
    if len(search_keywords) == 0:
        return False
    results = []
    for keyword in search_keywords:
        if isinstance(keyword, str):
            result = keyword.lower() in phrase.lower()
            results.append(result)
            if result:
                break
        elif isinstance(keyword, list):
            result = check_all_keywords_in_text(
                phrase=phrase,
                search_keywords=keyword,
            )
            results.append(result)
    return any(results)


def check_search_criteria(
    phrase: str,
    *,
    search_keywords: list[Any],
) -> bool:
    """Return `True` if `phrase` meets the search criteria defined by `search_keywords`."""
    return check_any_keywords_in_text(
        phrase=phrase,
        search_keywords=search_keywords,
    )


##
## === FORMATTING
##


def as_set_notation(
    search_keywords: list[Any] | str,
    *,
    set_level: int = 0,
) -> str:
    """Return `search_keywords` formatted as a human-readable set-notation string."""
    while isinstance(search_keywords, list) and (len(search_keywords) == 1):
        search_keywords = search_keywords[0]
        set_level += 1
    if not isinstance(search_keywords, list):
        return f"`{search_keywords}`"
    if set_level % 2 == 1:
        operator = " AND "
    else:
        operator = " OR "
    parts = []
    for keyword in search_keywords:
        if isinstance(keyword, list):
            inner = as_set_notation(
                keyword,
                set_level=set_level + 1,
            )
            parts.append(f"({inner})")
        else:
            parts.append(f"`{keyword}`")
    return operator.join(parts)


def print_search_criteria(
    search_config: dict[str, Any],
) -> None:
    """Print the include/exclude keywords and tracked authors from `search_config`."""
    keywords_to_include = search_config["keywords_to_include"]
    keywords_to_exclude = search_config["keywords_to_exclude"]
    authors = search_config["authors"]
    print("> including articles with phrases:")
    print(as_set_notation(keywords_to_include))
    print(" ")
    if len(keywords_to_exclude) > 0:
        print("> excluding articles with phrases:")
        print(as_set_notation(keywords_to_exclude))
        print(" ")
    if len(authors) > 0:
        print("> including articles with authors:", end="")
        print("\n\t- " + "\n\t- ".join(authors))
        print(" ")


## } MODULE
