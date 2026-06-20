## { MODULE

##
## === DEPENDENCIES
##

## stdlib
import os
from pathlib import Path

##
## === DIRECTORIES
##


def _find_project_root() -> Path:
    """Walk up from cwd looking for the repo root (pyproject.toml + configs/); fall back to ARXIVSCRAPER_ROOT."""
    for directory in [Path.cwd(), *Path.cwd().parents]:
        if (directory / "pyproject.toml").is_file() and (directory / "configs").is_dir():
            return directory
    env_root = os.environ.get("ARXIVSCRAPER_ROOT")
    if env_root:
        return Path(env_root).resolve()
    raise RuntimeError(
        "could not find the arXivScraper project root. "
        "Run from within the repo, or set ARXIVSCRAPER_ROOT to the repo path.",
    )


PROJECT_ROOT = _find_project_root()
configs_dir = PROJECT_ROOT / "configs"
search_configs_dir = configs_dir / "search"
ai_configs_dir = configs_dir / "ai"
md_files_dir = PROJECT_ROOT / "md_files"
pdfs_dir = PROJECT_ROOT / "pdfs"

## } MODULE
