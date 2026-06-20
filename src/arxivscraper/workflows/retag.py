## { SCRIPT

##
## === DEPENDENCIES
##

## stdlib
import sys
from pathlib import Path
from typing import Any

## local
from arxivscraper.config_paths import directories
from arxivscraper.support import articles, search_criteria

##
## === CONFIG LOADING
##


def _load_all_configs(
    *,
    config_dir: Path,
) -> dict[str, dict[str, Any]]:
    """Load every `.toml` search config from `config_dir`; return dict keyed by config name."""
    configs = {}
    for config_path in sorted(config_dir.glob("*.toml")):
        config_name = config_path.stem
        configs[config_name] = search_criteria.read_search_criteria(
            directory=config_dir,
            config_name=config_name,
        )
    return configs


##
## === KEYWORD MATCHING
##


def _article_matches_config(
    *,
    article: articles.Article,
    config: dict[str, Any],
) -> bool:
    """Return `True` if `article` title or abstract matches `config` keyword criteria."""
    text_title = (article.title or "").lower()
    text_abstract = (article.abstract or "").lower()
    exclude_keywords = config["keywords_to_exclude"]
    include_keywords = config["keywords_to_include"]
    if search_criteria.check_search_criteria(phrase=text_title, search_keywords=exclude_keywords):
        return False
    if search_criteria.check_search_criteria(phrase=text_abstract, search_keywords=exclude_keywords):
        return False
    return (
        search_criteria.check_search_criteria(phrase=text_title, search_keywords=include_keywords)
        or search_criteria.check_search_criteria(phrase=text_abstract, search_keywords=include_keywords)
    )


##
## === RETAG
##


def retag_articles(
    *,
    articles_list: list[articles.Article],
    configs: dict[str, dict[str, Any]],
) -> int:
    """Re-evaluate config tags for every article; save only those that changed. Returns count updated."""
    known_config_tags = {f"#{name}" for name in configs}
    num_updated = 0
    for article in articles_list:
        matching_tags = {
            f"#{config_name}"
            for config_name, config in configs.items()
            if _article_matches_config(article=article, config=config)
        }
        ## keep editorial tags (those not tied to any known config file)
        editorial_tags = [tag for tag in article.config_tags if tag not in known_config_tags]
        new_tags = sorted(matching_tags) + [t for t in editorial_tags if t not in matching_tags]
        if set(new_tags) == set(article.config_tags):
            continue
        article.config_tags = new_tags
        articles.save_article(article, force=True)
        num_updated += 1
    return num_updated


##
## === PROGRAM MAIN
##


def main() -> None:
    print("Loading search configs...")
    configs = _load_all_configs(config_dir=directories.search_configs_dir)
    print(f"Found {len(configs)} config(s): {', '.join(sorted(configs))}.")
    print("Reading in all articles...")
    articles_list = articles.read_all_markdown_files()
    print(f"Retagging {len(articles_list)} articles...")
    num_updated = retag_articles(articles_list=articles_list, configs=configs)
    print(f"Updated tags on {num_updated} article(s).")


##
## === ENTRY POINT
##

if __name__ == "__main__":
    main()
    sys.exit(0)

## } SCRIPT
