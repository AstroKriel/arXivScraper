## ###############################################################
## DEPENDANCIES
## ###############################################################
from arXivScraper.utils import ww_file_io


## ###############################################################
## READ SEARCH CRITERIA
## ###############################################################
def read_search_criteria(directory, config_name):
  required_keys = {
    "authors",
    "categories",
    "keywords_to_exclude",
    "keywords_to_include"
  }
  config = ww_file_io.read_file(f"{directory}/{config_name}.json", ".json")
  missing_keys = required_keys - required_keys
  if len(missing_keys) > 0:
    print(f"The following config keys are missing:")
    print("\t", ", ".join(missing_keys), "\n")
    raise Exception("Error: Config file is missing search keys")
  return config


## ###############################################################
## APPLY SEARCH CRITERIA
## ###############################################################
def does_text_contain_all_keywords(phrase, search_keywords):
  if len(search_keywords) == 0: return False
  results = []
  for keyword in search_keywords:
    if isinstance(keyword, str):
      result = keyword.lower() in phrase
      results.append(result)
    elif isinstance(keyword, list):
      result = does_text_contain_any_keywords(phrase, keyword)
      results.append(result)
  return all(results)

def does_text_contain_any_keywords(phrase, search_keywords):
  if len(search_keywords) == 0: return False
  results = []
  for keyword in search_keywords:
    if isinstance(keyword, str):
      result = keyword.lower() in phrase.lower()
      results.append(result)
      if result: break
    elif isinstance(keyword, list):
      result = does_text_contain_all_keywords(phrase, keyword)
      results.append(result)
  return any(results)

def meets_search_criteria(phrase, search_keywords):
  return does_text_contain_any_keywords(phrase, search_keywords)


## ###############################################################
## PRINT SEARCH CRITERIA
## ###############################################################
def search_keywords_to_set_notation(search_keywords, set_level=0):
  while isinstance(search_keywords, list) and (len(search_keywords) == 1):
    search_keywords = search_keywords[0]
    set_level += 1
  if not isinstance(search_keywords, list): return f"`{search_keywords}`"
  if set_level % 2 == 1: operator = " AND "
  else: operator = " OR "
  return operator.join(
    f"({search_keywords_to_set_notation(keyword, set_level+1)})"
    if isinstance(keyword, list)
    else f"`{keyword}`"
    for keyword in search_keywords
  )

def print_search_criteria(search_config):
  include_keywords = search_config["include_keywords"]
  exclude_keywords = search_config["exclude_keywords"]
  authors          = search_config["authors"]
  print("> including articles with phrases:")
  print(search_keywords_to_set_notation(include_keywords))
  print(" ")
  if len(exclude_keywords) > 0:
    print("> excluding articles with phrases:")
    print(search_keywords_to_set_notation(exclude_keywords))
    print(" ")
  if len(authors) > 0:
    print("> including articles with authors:", end="")
    print("\n\t- " + "\n\t- ".join(authors))
    print(" ")
  return


## END OF MODULE