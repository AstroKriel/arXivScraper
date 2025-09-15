## ###############################################################
## DEPENDENCIES
## ###############################################################

import sys
from arxivscraper.utils import filter_utils


## ###############################################################
## HELPER FUNCTION
## ###############################################################

def print_heading(str):
  print(str)
  print("=" * len(str))


## ###############################################################
## DEMO PROGRAM
## ###############################################################

def main():
  phrases = [
    f"the {animal} {action} over the {object}"
    for animal in [ "fox", "turtle", "cow" ]
    for action in [ "jumped", "leaped" ]
    for object in [ "moon", "log", "river" ]
  ]
  print_heading("List of phrases:")
  print("\n".join(phrases))
  print(" ")
  search_conditions = [
    [ "fox", ["jumped", "river"] ], # "fox" AND ("jumped" OR "river")
  ]
  print_heading("Search condition:")
  print(filter_utils.search_keywords_to_set_notation(search_conditions))
  print(" ")
  print_heading("List of phrases that met the search conditions:")
  for phrase in phrases:
    if filter_utils.meets_search_criteria(phrase, search_conditions):
      print(phrase)


## ###############################################################
## DEMO ENTRY POINT
## ###############################################################

if __name__ == "__main__":
  main()
  sys.exit(0)


## END OF DEMO PROGRAM