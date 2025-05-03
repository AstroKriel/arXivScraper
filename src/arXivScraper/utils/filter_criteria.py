## ###############################################################
## DEPENDANCIES
## ###############################################################
from arXivScraper.utils import file_io


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
  dict_config = file_io.read_file(f"{directory}/{config_name}.json", ".json")
  missing_keys = required_keys - required_keys
  if len(missing_keys) > 0:
    print(f"The following config keys are missing:")
    print("\t", ", ".join(missing_keys), "\n")
    raise Exception("Error: Config file is missing search keys")
  return dict_config


## ###############################################################
## APPLY SEARCH CRITERIA
## ###############################################################
def does_text_contain_all_keywords(phrase, list_search_keywords):
  if len(list_search_keywords) == 0: return False
  list_bools = []
  for keyword in list_search_keywords:
    if isinstance(keyword, str):
      bool_term_contained = keyword.lower() in phrase
      list_bools.append(bool_term_contained)
    elif isinstance(keyword, list):
      list_bools.append(
        does_text_contain_any_keywords(phrase, keyword)
      )
  return all(list_bools)

def does_text_contain_any_keywords(phrase, list_search_keywords):
  if len(list_search_keywords) == 0: return False
  list_bools = []
  for keyword in list_search_keywords:
    if isinstance(keyword, str):
      bool_term_contained = keyword.lower() in phrase.lower()
      list_bools.append(bool_term_contained)
      if bool_term_contained: break
    elif isinstance(keyword, list):
      list_bools.append(
        does_text_contain_all_keywords(phrase, keyword)
      )
  return any(list_bools)

def meets_search_criteria(phrase, list_search_conditions):
  return does_text_contain_any_keywords(phrase, list_search_conditions)


## ###############################################################
## PRINT SEARCH CRITERIA
## ###############################################################
def lols_to_set_notation(list_elems, set_level=0):
  while isinstance(list_elems, list) and (len(list_elems) == 1):
    list_elems = list_elems[0]
    set_level += 1
  if not isinstance(list_elems, list): return f"`{list_elems}`"
  if set_level % 2 == 1: operator = " AND "
  else: operator = " OR "
  return operator.join(
    f"({lols_to_set_notation(elem, set_level+1)})"
    if isinstance(elem, list)
    else f"`{elem}`"
    for elem in list_elems
  )

def print_search_criteria(dict_search):
  list_keywords_include = dict_search["list_keywords_include"]
  list_keywords_exclude = dict_search["list_keywords_exclude"]
  list_authors          = dict_search["list_authors"]
  print("> including articles with phrases:")
  print(lols_to_set_notation(list_keywords_include))
  print(" ")
  if len(list_keywords_exclude) > 0:
    print("> excluding articles with phrases:")
    print(lols_to_set_notation(list_keywords_exclude))
    print(" ")
  if len(list_authors) > 0:
    print("> including articles with authors:", end="")
    print("\n\t- " + "\n\t- ".join(list_authors))
    print(" ")
  return


## END OF HEADER FILE