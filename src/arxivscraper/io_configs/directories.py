## { MODULE

##
## === DEPENDENCIES
##

## stdlib
from pathlib import Path

##
## === DIRECTORIES
##

PROJECT_ROOT = Path(__file__).resolve().parents[3]
configs_dir  = PROJECT_ROOT / "configs"
md_files_dir = PROJECT_ROOT / "md_files"
pdfs_dir     = PROJECT_ROOT / "pdfs"

## } MODULE
