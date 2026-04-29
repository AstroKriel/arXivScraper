## { MODULE

##
## === DEPENDENCIES
##

## stdlib
import argparse
import re
from typing import Any

## local
from arxivscraper.io_configs import directories

##
## === USER INPUT HANDLER
##


class GetUserInputs:
    """Parse and validate CLI arguments for the main program, search, score, and fetch modes."""

    def __init__(
        self,
        include_main: bool = False,
        include_search: bool = False,
        include_fetch: bool = False,
        include_score: bool = False,
    ):
        self.parser = argparse.ArgumentParser(
            description="arXiv-Scraper: program to search for relevant arXiv papers.",
            formatter_class=lambda prog: argparse.RawDescriptionHelpFormatter(
                prog=prog,
                max_help_position=50,
            ),
        )
        if include_main:
            self._add_main_program_arguments()
        if include_search:
            self._add_search_arguments()
        if include_fetch:
            self._add_fetch_argument()
        if include_score:
            self._add_score_arguments()
        ## parse and store arguments
        name_space, _ = self.parser.parse_known_args()
        self.args = vars(name_space)

    def _add_main_program_arguments(
        self,
    ):
        """Sets up main program flag arguments."""
        parse_flags = self.parser.add_argument_group(description="Main program flags:")
        for short_flag, long_flag in [("-s", "--search"), ("-f", "--fetch"), ("-r", "--score"),
                                      ("-p", "--print"), ("-d", "--download")]:
            parse_flags.add_argument(
                short_flag,
                long_flag,
                default=False,
                required=False,
                action="store_true",
                help="Type: bool, default: %(default)s",
            )

    def _add_search_arguments(
        self,
    ):
        """Sets up search-specific arguments."""
        search_args = self.parser.add_argument_group(
            description="Search arguments (relevant when main program is run with `-s`):",
        )
        search_args.add_argument(
            "-c",
            "--config_name",
            type=str,
            required=False,
            metavar="",
            help="Name of the config-file that defines search parameters.",
        )
        search_args.add_argument(
            "-lb",
            "--lookback_days",
            type=int,
            required=False,
            metavar="",
            help="Lookback period (in days) to start search.",
        )

    def _add_fetch_argument(
        self,
    ):
        """Sets up fetch-specific arguments."""
        fetch_args = self.parser.add_argument_group(
            description="Fetch argument (relevant when running with `-f`):",
        )
        fetch_args.add_argument(
            "-id",
            type=str,
            required=False,
            metavar="",
            help="arXiv ID in the format `2310.17036`.",
        )

    def _add_score_arguments(
        self,
    ):
        """Sets up score-specific arguments."""
        score_args = self.parser.add_argument_group(
            description="Score arguments (relevant when running with `-r`):",
        )
        score_args.add_argument(
            "--model",
            type=str,
            required=False,
            metavar="",
            help="Model name override (e.g. 'gpt-4o-mini', 'llama3.2'). Overrides ai_provider.json.",
        )
        score_args.add_argument(
            "--base-url",
            type=str,
            required=False,
            metavar="",
            dest="base_url",
            help="API base URL override (e.g. 'http://localhost:11434/v1'). Overrides ai_provider.json.",
        )

    def get_program_inputs(
        self,
    ):
        """Returns main program flags, and ensures at least one is set."""
        main_flags = ["search", "fetch", "score", "download"]
        if not any(self.args.get(flag) for flag in main_flags):
            print(
                "Error: At least one of the following flags must be provided: --search, --fetch, --score, --download\n",
            )
            self.parser.print_help()
        return {key: self.args.get(key) for key in ["search", "fetch", "score", "print", "download"]}

    def get_search_inputs(
        self,
    ) -> dict[str, Any]:
        """Returns only the search-specific arguments and prompts for any missing parameters if required."""
        ## collect relevant search-related arguments
        search_args = {
            key: self.args.get(key)
            for key in [
                "config_name",
                "lookback_days",
            ]
        }
        ## prompt for missing values
        if not search_args["config_name"]:
            search_args["config_name"] = input("Please provide --config_name: ")
        config_name = search_args["config_name"]
        config_path = directories.configs_dir / f"{config_name}.json"
        if not config_path.exists():
            raise FileNotFoundError(
                f"config file not found: `{config_name}.json`; searched in {directories.configs_dir}.",
            )
        if search_args["lookback_days"] is None:
            search_args["lookback_days"] = int(input("Please provide --lookback_days: "))
        return search_args

    def get_score_inputs(
        self,
    ) -> dict[str, Any]:
        """Returns score-specific CLI overrides (model, base_url). None values mean 'use config file'."""
        return {key: self.args.get(key) for key in ["model", "base_url"]}

    def get_fetch_inputs(
        self,
    ):
        """Returns only the fetch-specific arguments, prompting if the arXiv ID is not passed, and validates the ID-format."""
        arxiv_id = self.args.get("id")
        ## prompt for missing value
        if arxiv_id is None:
            print("Which article do you want to fetch from the arXiv?")
            arxiv_id = input("Enter an arXiv ID (e.g., `2310.17036`): ")
        print(" ")
        ## check the arXiv ID follows the right format
        re_pattern = r"^\d{4}\.\d{4,5}$"
        if not re.match(
                pattern=re_pattern,
                string=arxiv_id,
        ):
            raise ValueError(
                f"`arxiv_id` must match the format `2310.17036`; got `{arxiv_id}`.",
            )
        return arxiv_id


## } MODULE
