## { MODULE

##
## === DEPENDENCIES
##

## stdlib
import datetime
import sys
import time

## local
from arxivscraper.routines import download_articles as DownloadArticles
from arxivscraper.routines import fetch_from_arxiv as FetchFromArxiv
from arxivscraper.routines import score_articles as ScoreArticle
from arxivscraper.routines import search_arxiv as SearchArxiv
from arxivscraper.utils import argparse_utils

##
## === MAIN
##


def main():
    time_start = time.time()
    print(
        "Program started at {}".format(
            datetime.datetime.now().strftime("%H:%M:%S"),
        ),
    )
    obj_user_inputs = argparse_utils.GetUserInputs(
        include_main=True,
        include_search=True,
        include_fetch=True,
    )
    dict_program_flags = obj_user_inputs.get_program_inputs()
    if dict_program_flags["search"]:
        SearchArxiv.main()
        if dict_program_flags["score"]: ScoreArticle.main()
    elif dict_program_flags["score"]: ScoreArticle.main()
    elif dict_program_flags["fetch"]: FetchFromArxiv.main()
    elif dict_program_flags["download"]: DownloadArticles.main()
    time_elapsed = time.time() - time_start
    print(f"Elapsed time: {time_elapsed:.2f} seconds.")


##
## === ENTRY POINT
##

if __name__ == "__main__":
    main()
    sys.exit(0)

## } MODULE
