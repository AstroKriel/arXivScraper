## { MODULE

##
## === DEPENDENCIES
##

## stdlib
import os
from pathlib import Path

## personal
from huginn import manage_log

##
## === DIRECTORIES
## every path sits under `ARXIVSCRAPER_ROOT`, read when a command first needs a path, so `--help` works without it.
##


def get_project_root() -> Path:
    project_root_text = os.environ.get("ARXIVSCRAPER_ROOT")
    if not project_root_text:
        manage_log.exit_with_error(
            "ARXIVSCRAPER_ROOT is not set; add `export ARXIVSCRAPER_ROOT=/path/to/arXivScraper` to your shell profile",
        )
    return Path(project_root_text).resolve()


def get_search_configs_dir() -> Path:
    return get_project_root() / "configs" / "search"


def get_ai_configs_dir() -> Path:
    return get_project_root() / "configs" / "ai"


def get_md_files_dir() -> Path:
    return get_project_root() / "md_files"


def get_pdfs_dir() -> Path:
    return get_project_root() / "pdfs"


## } MODULE
