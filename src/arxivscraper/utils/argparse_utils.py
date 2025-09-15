## ###############################################################
## DEPENDENCIES
## ###############################################################

import sys
import re
import argparse
from arxivscraper.io_configs import directories


## ###############################################################
## GROUP DIFFERENT TYPES OF USER INPUTS
## ###############################################################

class GetUserInputs:

  def __init__(
      self,
      include_main   = False,
      include_search = False,
      include_fetch  = False,
    ):
    self.parser = argparse.ArgumentParser(
      description     = "arXiv-Scraper: program to search for relevant arXiv papers.",
      formatter_class = lambda prog: argparse.RawDescriptionHelpFormatter(prog, max_help_position=50),
    )
    if include_main:   self._add_main_program_arguments()
    if include_search: self._add_search_arguments()
    if include_fetch:  self._add_fetch_argument()
    ## parse and store arguments
    name_space, _extras = self.parser.parse_known_args()
    self.args = vars(name_space)

  def _add_main_program_arguments(self):
    """Sets up main program flag arguments."""
    main_args = {
      "default"  : False,
      "required" : False,
      "action"   : "store_true",
      "help"     : "Type: bool, default: %(default)s"
    }
    parse_flags = self.parser.add_argument_group(description="Main program flags:")
    parse_flags.add_argument("-s", "--search",   **main_args)
    parse_flags.add_argument("-f", "--fetch",    **main_args)
    parse_flags.add_argument("-r", "--score",    **main_args)
    parse_flags.add_argument("-p", "--print",    **main_args)
    parse_flags.add_argument("-d", "--download", **main_args)

  def _add_search_arguments(self):
    """Sets up search-specific arguments."""
    search_args = self.parser.add_argument_group(description="Search arguments (relevant when main program is run with `-s`):")
    search_args.add_argument("-c",  "--config_name",   type=str, required=False, metavar="", help="Name of the config-file that defines search parameters.")
    search_args.add_argument("-lb", "--lookback_days", type=int, required=False, metavar="", help="Lookback period (in days) to start search.")

  def _add_fetch_argument(self):
    """Sets up fetch-specific arguments."""
    fetch_args = self.parser.add_argument_group(description="Fetch argument (relevant when running with `-f`):")
    fetch_args.add_argument("-id", type=str, required=False, metavar="", help="arXiv ID in the format `2310.17036`.")

  def get_program_inputs(self):
    """Returns main program flags, and ensures at least one is set."""
    main_flags = ["search", "fetch", "score", "download"]
    if not any(self.args.get(flag) for flag in main_flags):
      print("Error: At least one of the following flags must be provided: --search, --fetch, --score, --download\n")
      self.parser.print_help()
      sys.exit(2)
    return {
      key: self.args.get(key)
      for key in ["search", "fetch", "score", "print", "download"]
    }

  def get_search_inputs(self):
    """Returns only the search-specific arguments and prompts for any missing parameters if required."""
    ## collect relevant search-related arguments
    search_args = {
      key: self.args.get(key)
      for key in [
        "config_name",
        "lookback_days"
      ]
    }
    ## prompt for missing values
    if not search_args["config_name"]:
      search_args["config_name"] = input("Please provide --config_name: ")
    config_name = search_args["config_name"]
    config_path = directories.search_configs / f"{config_name}.json"
    if not config_path.exists():
      raise Exception(f"Error: Config file `{config_name}.json` does not exist under: {directories.search_configs}")
    if search_args["lookback_days"] is None:
      search_args["lookback_days"] = int(input("Please provide --lookback_days: "))
    return search_args

  def get_fetch_inputs(self):
    """Returns only the fetch-specific arguments, prompting if the arXiv ID is not passed, and validates the ID-format."""
    arxiv_id = self.args.get("id")
    ## prompt for missing value
    if arxiv_id is None:
      print("Which article do you want to fetch from the arXiv?")
      arxiv_id = input("Enter an arXiv ID (e.g., `2310.17036`): ")
    print(" ")
    ## check the arXiv ID follows the right format
    re_pattern = r"^\d{4}\.\d{4,5}$"
    if not re.match(re_pattern, arxiv_id):
      raise Exception(f"The ID you entered `{arxiv_id}` was invalid. Please enter it in the format `2310.17036`.")
    return arxiv_id


## END OF MODULE