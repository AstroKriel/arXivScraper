## ###############################################################
## LOAD MODULES
## ###############################################################
import sys, time, datetime

from src.headers import Directories
from src.headers import FileNames
from src.headers import IO
from src.headers import WWFnFs
from src.headers import WWDates
from src.headers import WWArgParse
from src.headers import WWArticles

from src.scripts import search_arxiv as SearchArxiv
from src.scripts import score_article as ScoreArticle
from src.scripts import fetch_from_arxiv as FetchFromArxiv
from src.scripts import download_articles as DownloadArticles


## ###############################################################
## OPERATOR CLASS
## ###############################################################
class ArxivScraper():
  def __init__(self, obj_user_inputs: WWArgParse.GetUserInputs):
    self.obj_user_inputs = obj_user_inputs

  def searchArxiv(self):
    dict_search_params = self.obj_user_inputs.getSearchInputs()
    obj_search_arxiv = SearchArxiv.SearchArxiv(
      current_date  = WWDates.getDateToday(),
      lookback_date = WWDates.getDateNDaysAgo(dict_search_params["lookback_days"]),
      config_name   = dict_search_params["config_name"],
    )
    obj_search_arxiv.search()
    return obj_search_arxiv.getSortedArticles()

  def fetchFromArxiv(self):
    arxiv_id = self.obj_user_inputs.getFetchInputs()
    article_dict = FetchFromArxiv.fetchFromArxiv(arxiv_id)
    return article_dict

  def scoreArticles(self, list_article_dicts):
    num_articles    = len(list_article_dicts)
    prompt_rules    = IO.readTextFile(f"{Directories.directory_config}/{FileNames.filename_ai_rules}")
    prompt_criteria = IO.readTextFile(f"{Directories.directory_config}/{FileNames.filename_ai_criteria}")
    for article_index, dict_article in enumerate(list_article_dicts):
      print(f"({article_index+1}/{num_articles})")
      bool_scored = ScoreArticle.getAIScore(
        dict_article    = dict_article,
        prompt_rules    = prompt_rules,
        prompt_criteria = prompt_criteria,
      )
      if bool_scored: WWArticles.saveArticle2Markdown(dict_article)
      print(" ")

  def printArticles(self, list_article_dicts):
    num_articles = len(list_article_dicts)
    print(f"Found {num_articles} articles:\n")
    for article_index, dict_article in enumerate(list_article_dicts):
      print(f"({article_index+1}/{num_articles})")
      WWArticles.printArticle(dict_article)
      print(" ")

  def saveArticles(self, list_article_dicts):
    WWFnFs.createDirectory(Directories.directory_mdfiles, bool_add_space=True)
    num_articles = len(list_article_dicts)
    for dict_article in list_article_dicts:
      WWArticles.saveArticle2Markdown(dict_article, bool_verbose=False)
    ## TODO: check which articles are new and need to be saved
    print(f"Saved {num_articles} articles.")
    print(" ")

  def downloadPDFs(self):
    WWFnFs.createDirectory(Directories.directory_pdfs, bool_add_space=True)
    list_article_dicts = WWArticles.readAllMarkdownFiles()
    DownloadArticles.downloadPDFs(list_article_dicts)


## ###############################################################
## MAIN PROGRAM
## ###############################################################
def main():
  time_start = time.time()
  print("Program started at {}".format(
    datetime.datetime.now().strftime("%H:%M:%S")
  ))
  obj_user_inputs = WWArgParse.GetUserInputs()
  dict_program_flags = obj_user_inputs.getMainProgramInputs()
  obj_arxiv_scraper = ArxivScraper(obj_user_inputs)
  if dict_program_flags["search"]:
    list_article_dicts = obj_arxiv_scraper.searchArxiv()
    obj_arxiv_scraper.saveArticles(list_article_dicts)
    if dict_program_flags["score"]: obj_arxiv_scraper.scoreArticles(list_article_dicts)
    if dict_program_flags["print"]: obj_arxiv_scraper.printArticles(list_article_dicts)
  elif dict_program_flags["score"]:
    list_article_dicts = WWArticles.readAllMarkdownFiles()
    obj_arxiv_scraper.scoreArticles(list_article_dicts)
  elif dict_program_flags["fetch"]:
    dict_article = obj_arxiv_scraper.fetchFromArxiv()
    if (dict_article is not None) and dict_program_flags["download"]:
      DownloadArticles.downloadPDF(dict_article)
    print(" ")
  elif dict_program_flags["download"]: obj_arxiv_scraper.downloadPDFs()
  time_elapsed = time.time() - time_start
  print(f"Elapsed time: {time_elapsed:.2f} seconds.")


## ###############################################################
## PROGRAM ENTRY POINT
## ###############################################################
if __name__ == "__main__":
  main()
  sys.exit(0)


## END OF PROGRAM