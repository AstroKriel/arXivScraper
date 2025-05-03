## ###############################################################
## LOAD MODULES
## ###############################################################
import sys
import time
import datetime
from arXivScraper.utils import file_io, dates, articles, user_inputs
from arXivScraper.config import directories, file_names
from arXivScraper.routines import search_arxiv as SearchArxiv
from arXivScraper.routines import score_articles as ScoreArticle
from arXivScraper.routines import fetch_from_arxiv as FetchFromArxiv
from arXivScraper.routines import download_articles as DownloadArticles


## ###############################################################
## OPERATOR CLASS
## ###############################################################
class ArxivScraper():
  def __init__(self, obj_user_inputs: user_inputs.GetUserInputs):
    self.obj_user_inputs = obj_user_inputs

  def search_arxiv(self):
    dict_search_params = self.obj_user_inputs.get_search_nputs()
    obj_search_arxiv = SearchArxiv.SearchArxiv(
      current_date  = dates.get_date_today(),
      lookback_date = dates.get_date_n_days_ago(dict_search_params["lookback_days"]),
      config_name   = dict_search_params["config_name"],
    )
    obj_search_arxiv.search()
    return obj_search_arxiv.get_sorted_articles()

  def fetch_from_arxiv(self):
    arxiv_id = self.obj_user_inputs.get_fetch_inputs()
    article_dict = FetchFromArxiv.fetch_from_arxiv(arxiv_id)
    return article_dict

  def score_articles(self, list_article_dicts):
    num_articles    = len(list_article_dicts)
    prompt_rules    = file_io.read_text_file(f"{directories.config}/{file_names.ai_rules}")
    prompt_criteria = file_io.read_text_file(f"{directories.config}/{file_names.ai_criteria}")
    for article_index, dict_article in enumerate(list_article_dicts):
      print(f"({article_index+1}/{num_articles})")
      bool_scored = ScoreArticle.get_ai_score(
        dict_article    = dict_article,
        prompt_rules    = prompt_rules,
        prompt_criteria = prompt_criteria,
      )
      if bool_scored: articles.save_article(dict_article)
      print(" ")

  def print_articles(self, list_article_dicts):
    num_articles = len(list_article_dicts)
    print(f"Found {num_articles} articles:\n")
    for article_index, dict_article in enumerate(list_article_dicts):
      print(f"({article_index+1}/{num_articles})")
      articles.print_article(dict_article)
      print(" ")

  def save_articles(self, list_article_dicts):
    file_io.init_directory(directories.mdfiles, bool_add_space=True)
    num_articles = len(list_article_dicts)
    for dict_article in list_article_dicts:
      articles.save_article(dict_article, bool_verbose=False)
    ## TODO: check which articles are new and need to be saved
    print(f"Saved {num_articles} articles.")
    print(" ")

  def download_pdfs(self):
    file_io.init_directory(directories.pdfs, bool_add_space=True)
    list_article_dicts = articles.read_all_markdown_files()
    DownloadArticles.download_pdfs(list_article_dicts)


## ###############################################################
## MAIN PROGRAM
## ###############################################################
def main():
  time_start = time.time()
  print("Program started at {}".format(
    datetime.datetime.now().strftime("%H:%M:%S")
  ))
  obj_user_inputs = user_inputs.GetUserInputs()
  dict_program_flags = obj_user_inputs.get_program_inputs()
  obj_arxiv_scraper = ArxivScraper(obj_user_inputs)
  if dict_program_flags["search"]:
    list_article_dicts = obj_arxiv_scraper.search_arxiv()
    obj_arxiv_scraper.save_articles(list_article_dicts)
    if dict_program_flags["score"]: obj_arxiv_scraper.score_articles(list_article_dicts)
    if dict_program_flags["print"]: obj_arxiv_scraper.print_articles(list_article_dicts)
  elif dict_program_flags["score"]:
    list_article_dicts = articles.read_all_markdown_files()
    obj_arxiv_scraper.score_articles(list_article_dicts)
  elif dict_program_flags["fetch"]:
    dict_article = obj_arxiv_scraper.fetch_from_arxiv()
    if (dict_article is not None) and dict_program_flags["download"]:
      DownloadArticles.download_pdf(dict_article)
    print(" ")
  elif dict_program_flags["download"]: obj_arxiv_scraper.download_pdfs()
  time_elapsed = time.time() - time_start
  print(f"Elapsed time: {time_elapsed:.2f} seconds.")


## ###############################################################
## PROGRAM ENTRY POINT
## ###############################################################
if __name__ == "__main__":
  main()
  sys.exit(0)


## END OF PROGRAM