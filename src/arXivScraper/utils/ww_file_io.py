## ###############################################################
## DEPENDANCIES
## ###############################################################

import os
import json
import yaml


## ###############################################################
## READING FILES
## ###############################################################

def file_exists(file_path):
  return os.path.isfile(file_path)

def init_directory(directory):
  if not(os.path.exists(directory)):
    os.makedirs(directory)
    print(f"Successfully initialised directory: {directory}")
    print(" ")
  return

def read_file(file_path, expected_extension):
  if not file_path.endswith(expected_extension):
    raise ValueError(f"File must use a `{expected_extension}` extension. Input: {file_path}")
  try:
    with open(file_path, "r", encoding="utf-8") as file_pointer:
      if   expected_extension == ".json":         return json.load(file_pointer)
      elif expected_extension == ".yaml":         return yaml.safe_load(file_pointer)
      elif expected_extension in [".txt", ".md"]: return file_pointer.read()
      else: raise NotImplementedError(f"Unsupported file extension: {expected_extension}")
  except Exception as e:
    raise IOError(f"Error reading {file_path}: {e}")

def read_text_file(file_path):
  return read_file(file_path, expected_extension=".txt")

def read_markdown_file(file_path):
  return read_file(file_path, expected_extension=".md")

def read_yaml_file(file_path):
  return read_file(file_path, expected_extension=".yaml")


## END OF MODULE