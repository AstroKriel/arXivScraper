## { MODULE

##
## === DEPENDENCIES
##

## stdlib
import tomllib
from pathlib import Path
from typing import Any

## third-party
import yaml

##
## === FILE I/O
##


def create_directory(
    directory: Path,
) -> None:
    """Create `directory` and any missing parents; do nothing if it already exists."""
    directory.mkdir(
        parents=True,
        exist_ok=True,
    )


def read_file(
    file_path: Path,
    *,
    expected_extension: str,
) -> Any:
    """Read and return the contents of `file_path`, dispatching on extension."""
    received_extension = file_path.suffix.lower()
    if received_extension != expected_extension:
        raise ValueError(
            f"`expected_extension` must be `{expected_extension}`; got `{received_extension}`.",
        )
    if not file_path.is_file():
        raise FileNotFoundError(f"file not found: {file_path}.")
    try:
        if expected_extension == ".toml":
            with file_path.open("rb") as file_pointer:
                return tomllib.load(file_pointer)
        with file_path.open("r", encoding="utf-8") as file_pointer:
            if expected_extension == ".yaml":
                return yaml.safe_load(file_pointer)
            elif expected_extension in (".txt", ".md"):
                return file_pointer.read()
            else:
                raise NotImplementedError(f"unsupported file extension: `{expected_extension}`.")
    except (ValueError, FileNotFoundError, NotImplementedError):
        raise
    except Exception as error:
        raise IOError(f"error reading {file_path}.") from error


def read_text_file(
    file_path: Path,
) -> str:
    """Read and return the contents of a `.txt` file at `file_path`."""
    return read_file(
        file_path,
        expected_extension=".txt",
    )


def read_markdown_file(
    file_path: Path,
) -> str:
    """Read and return the contents of a `.md` file at `file_path`."""
    return read_file(
        file_path,
        expected_extension=".md",
    )


def read_toml_file(
    file_path: Path,
) -> Any:
    """Read and return the parsed contents of a `.toml` file at `file_path`."""
    return read_file(
        file_path,
        expected_extension=".toml",
    )


def read_yaml_file(
    file_path: Path,
) -> Any:
    """Read and return the parsed contents of a `.yaml` file at `file_path`."""
    return read_file(
        file_path,
        expected_extension=".yaml",
    )


## } MODULE
