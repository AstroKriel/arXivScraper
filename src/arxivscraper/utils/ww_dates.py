## ###############################################################
## DEPENDENCIES
## ###############################################################

import datetime


## ###############################################################
## HELPER FUNCTIONS TO WORK WITH DATES
## ###############################################################

def cast_date_to_string(date):
  str_year  = str(date.year).zfill(4)
  str_month = str(date.month).zfill(2)
  str_day   = str(date.day).zfill(2)
  return f"{str_year}-{str_month}-{str_day}"

def cast_string_to_date(str_date):
  return datetime.datetime.strptime(str_date, "%Y-%m-%d").date()

def get_date_today():
  return datetime.datetime.now()

def get_date_n_days_ago(num_days):
  date_today = datetime.datetime.now()
  date_delta = datetime.timedelta(days=int(num_days))
  date_ago  = date_today - date_delta
  return date_ago


## END OF MODULE