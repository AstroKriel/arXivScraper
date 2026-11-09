## { SCRIPT

##
## === DEPENDENCIES
##

## stdlib
from pathlib import Path
from typing import Any

## personal
from huginn import manage_log, manage_shell

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
    for config_name in search_criteria.list_profile_names(config_dir):
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
) -> list[articles.Article]:
    """Re-evaluate config tags for every article; update the tags in place and return the articles that changed."""
    known_config_tags = {f"#{_name}" for _name in configs}
    retagged_articles: list[articles.Article] = []
    for article in articles_list:
        matching_tags = {
            f"#{_config_name}"
            for _config_name, _config in configs.items()
            if _article_matches_config(article=article, config=_config)
        }
        ## keep editorial tags (those not tied to any known config file)
        editorial_tags = [_tag for _tag in article.config_tags if _tag not in known_config_tags]
        new_tags = sorted(matching_tags) + [_tag for _tag in editorial_tags if _tag not in matching_tags]
        if set(new_tags) == set(article.config_tags):
            continue
        article.config_tags = new_tags
        retagged_articles.append(article)
    return retagged_articles


def _save_articles(
    articles_list: list[articles.Article],
) -> None:
    ## each article was read from its own file, so it is written back as it is; merging would restore removed tags
    for article in articles_list:
        articles.write_article_file(article)


##
## === COMMAND
##


def cmd_retag() -> None:
    """Re-check every saved paper against every search profile, and save the papers whose tags changed."""
    manage_log.log_task("reading the search profiles")
    configs = _load_all_configs(config_dir=directories.get_search_configs_dir())
    manage_log.log_outcome(
        f"found {len(configs)} search profiles",
        status=manage_log.OutcomeStatus.SUCCESS,
        items={"profiles": ", ".join(sorted(configs))},
    )
    manage_log.log_task("re-checking the tags of every saved paper")
    articles_list = articles.read_all_markdown_files()
    retagged_articles = retag_articles(
        articles_list=articles_list,
        configs=configs,
    )
    if not retagged_articles:
        manage_log.log_outcome(
            f"all {len(articles_list)} papers already have the right tags",
            status=manage_log.OutcomeStatus.SKIPPED,
        )
        return
    manage_shell.run_fn(
        description=f"save {len(retagged_articles)} retagged papers",
        fn=lambda: _save_articles(retagged_articles),
    )
    manage_log.log_outcome(
        f"retagged {len(retagged_articles)} of {len(articles_list)} papers",
        status=manage_log.OutcomeStatus.SUCCESS,
    )

## } SCRIPT
