## ###############################################################
## LOAD MODULES
## ###############################################################

import sys
import arxiv
import unidecode
from arxivscraper.utils import ww_file_io, ww_articles, ww_dates, ww_filter_criteria, ww_user_inputs
from arxivscraper.io_configs import directories


## ###############################################################
## OPPERATOR CLASS
## ###############################################################

class SearchArxiv():

  def __init__(self, lookback_date, current_date, config_name):
    self.lookback_date = lookback_date
    self.current_date  = current_date
    self.config_name   = config_name
    self.articles      = []

  def search(self):
    self._read_search_criteria()
    for search_category in self.dict_search_criteria["categories"]:
      print(f"Searching: {search_category}")
      print(f"Date range: {ww_dates.cast_date_to_string(self.lookback_date)} to {ww_dates.cast_date_to_string(self.current_date)}")
      self.client = arxiv.Client(
        page_size     = 200,
        delay_seconds = 1,
        num_retries   = 100
      )
      num_articles_looked_at_in_category = 0
      num_new_articles_saved_in_category = 0
      for arxiv_article in self.client.results(self._create_search_query(search_category)):
        self._display_progress(num_articles_looked_at_in_category)
        num_articles_looked_at_in_category += 1
        if not(self._is_within_date_range(arxiv_article)): break
        arxiv_id = str(arxiv_article.pdf_url).split("/")[-1].split("v")[0]
        if self._is_duplicate(arxiv_id): continue
        is_relevant, reasons = self._check_config_conditions(arxiv_article)
        if is_relevant:
          config_results = { self.config_name : reasons }
          article = ww_articles.get_article_summary(
            arxiv_article  = arxiv_article,
            config_results = config_results
          )
          self.articles.append(article)
          num_new_articles_saved_in_category += 1
      print(f"\nFound {num_new_articles_saved_in_category} interesting articles from the {num_articles_looked_at_in_category} looked at.\n")

  def get_sorted_articles(self):
    return sorted(
      self.articles,
      key     = lambda article: article.get("date_updated"),
      reverse = True
    )

  def _read_search_criteria(self):
    self.dict_search_criteria = ww_filter_criteria.read_search_criteria(
      directory   = directories.search_configs,
      config_name = self.config_name,
    )
    print(f"Searching for articles:")
    print("> from: {}".format(ww_dates.cast_date_to_string(self.lookback_date)))
    print("> to:   {}".format(ww_dates.cast_date_to_string(self.current_date)))
    print(" ")
    print(f"> using the `#{self.config_name}` config file")
    print(" ")
    ww_filter_criteria.print_search_criteria(self.dict_search_criteria)

  def _create_search_query(self, category):
    return arxiv.Search(
      query       = category,
      max_results = 10**4,
      sort_by     = arxiv.SortCriterion.SubmittedDate
    )

  def _is_within_date_range(self, arxiv_article):
    article_date = arxiv_article.updated.date()
    return (self.lookback_date.date() <= article_date) and (article_date <= self.current_date.date())

  def _is_duplicate(self, this_arxiv_id):
    return any([
      this_arxiv_id == article_dict["arxiv_id"]
      for article_dict in self.articles
    ])

  def _check_config_conditions(self, arxiv_article):
    if ww_filter_criteria.meets_search_criteria(arxiv_article.title.lower(), self.dict_search_criteria["exclude_keywords"]): return False, None
    title_passed = ww_filter_criteria.meets_search_criteria(arxiv_article.title.lower(), self.dict_search_criteria["include_keywords"])
    if ww_filter_criteria.meets_search_criteria(arxiv_article.summary.lower(), self.dict_search_criteria["exclude_keywords"]): return False, None
    abstract_passed = ww_filter_criteria.meets_search_criteria(arxiv_article.summary.lower(), self.dict_search_criteria["include_keywords"])
    author_last_names = [
      unidecode.unidecode(str(author).lower().split(" ")[-1])
      for author in arxiv_article.authors
    ]
    authors_passes = any(
      author.lower() in author_last_names
      for author in self.dict_search_criteria["authors"]
    )
    reasons = [ title_passed, abstract_passed, authors_passes ]
    return any(reasons), reasons

  def _display_progress(self, num_articles_looked_at_in_category):
    if num_articles_looked_at_in_category == 0: print("Progress:", end=" ")
    elif (num_articles_looked_at_in_category % 10) == 0: print("x", end="")
    elif (num_articles_looked_at_in_category % 50) == 0: print(" ", end="")


## ###############################################################
## ROUTINE MAIN
## ###############################################################

def main():
  obj_user_inputs = ww_user_inputs.GetUserInputs()
  dict_search_params = obj_user_inputs.get_search_nputs()
  obj_search_arxiv = SearchArxiv(
    current_date  = ww_dates.get_date_today(),
    lookback_date = ww_dates.get_date_n_days_ago(dict_search_params["lookback_days"]),
    config_name   = dict_search_params["config_name"],
  )
  obj_search_arxiv.search()
  articles = obj_search_arxiv.get_sorted_articles()
  ww_file_io.init_directory(directories.output_mdfiles)
  for article in articles:
    ww_articles.save_article(article, verbose=False, force=True)
  print(f"Saved {len(articles)} articles.")
  print(" ")


## ###############################################################
## ROUTINE ENTRY POINT
## ###############################################################

if __name__ == "__main__":
  main()
  sys.exit(0)


## END OF ROUTINE