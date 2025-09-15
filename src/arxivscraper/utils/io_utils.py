## ###############################################################
## DEPENDENCIES
## ###############################################################

import json
import yaml
from typing import Any
from pathlib import Path

## ###############################################################
## READING FILES
## ###############################################################


def init_directory(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)


def read_file(
    file_path: Path,
    expected_extension: str,
) -> Any:
    received_extension = file_path.suffix.lower()
    if received_extension != expected_extension:
        raise ValueError(f"File must use a `{expected_extension}` extension. Received: {file_path.name}")
    if not file_path.is_file():
        raise FileNotFoundError(f"File was not found: {file_path}")
    try:
        with file_path.open("r", encoding="utf-8") as fp:
            if expected_extension == ".json":
                return json.load(fp)
            elif expected_extension == ".yaml":
                return yaml.safe_load(fp)
            elif expected_extension in (".txt", ".md"):
                return fp.read()
            else:
                raise NotImplementedError(f"Unsupported file extension: {expected_extension}")
    except Exception as e:
        raise IOError(f"Error reading {file_path}: {e}")


def read_text_file(file_path: Path) -> str:
    return read_file(file_path, expected_extension=".txt")


def read_markdown_file(file_path: Path) -> str:
    return read_file(file_path, expected_extension=".md")


def read_yaml_file(file_path: Path) -> Any:
    return read_file(file_path, expected_extension=".yaml")


## END OF MODULE
