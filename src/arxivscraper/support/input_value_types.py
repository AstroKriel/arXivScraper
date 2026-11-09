## { MODULE

##
## === DEPENDENCIES
##

## stdlib
import argparse
import re
from typing import ClassVar

## personal
from huginn import cmd_args

## local
from arxivscraper.config_paths import directories

##
## === CONVERSIONS
## each one checks a value as it is typed, on the command line or as an answer to a question.
##


def _convert_str_to_arxiv_id(
    text: str,
) -> str:
    arxiv_id = text.strip()
    arxiv_id_is_valid = re.fullmatch(r"\d{4}\.\d{4,5}", arxiv_id) is not None
    if not arxiv_id_is_valid:
        raise argparse.ArgumentTypeError(f"arXiv id must look like `2310.17036`; got `{text}`.")
    return arxiv_id


def _convert_str_to_profile_name(
    text: str,
) -> str:
    profile_name = text.strip()
    search_configs_dir = directories.get_search_configs_dir()
    if not (search_configs_dir / f"{profile_name}.toml").is_file():
        profile_names = sorted(_config_path.stem for _config_path in search_configs_dir.glob("*.toml"))
        raise argparse.ArgumentTypeError(
            f"no search profile `{profile_name}` in {search_configs_dir}; profiles: {', '.join(profile_names)}.",
        )
    return profile_name


def _convert_str_to_tag(
    text: str,
) -> str:
    tag = text.strip().lower()
    if (tag == "") or (" " in tag):
        raise argparse.ArgumentTypeError(f"tag must be one word; got `{text}`.")
    return tag


##
## === INPUT VALUE TYPES
##


class InputValueTypes(cmd_args.InputValueTypes):
    ARXIV_ID: ClassVar[cmd_args.InputValueType] = cmd_args.InputValueType(
        placeholder_name="arxiv-id",
        convert_fn=_convert_str_to_arxiv_id,
    )
    PROFILE: ClassVar[cmd_args.InputValueType] = cmd_args.InputValueType(
        placeholder_name="profile",
        convert_fn=_convert_str_to_profile_name,
    )
    TAG: ClassVar[cmd_args.InputValueType] = cmd_args.InputValueType(
        placeholder_name="tag",
        convert_fn=_convert_str_to_tag,
    )


## } MODULE
