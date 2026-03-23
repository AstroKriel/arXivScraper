## { MODULE

##
## === DEPENDENCIES
##

## stdlib
import datetime

##
## === DATE HELPERS
##


def cast_date_to_string(
    date: datetime.date,
) -> str:
    str_year = str(date.year).zfill(4)
    str_month = str(date.month).zfill(2)
    str_day = str(date.day).zfill(2)
    return f"{str_year}-{str_month}-{str_day}"


def cast_string_to_date(
    str_date: str,
) -> datetime.date:
    return datetime.datetime.strptime(str_date, "%Y-%m-%d").date()


def get_date_today() -> datetime.datetime:
    return datetime.datetime.now()


def get_date_n_days_ago(
    num_days: int,
) -> datetime.datetime:
    date_today = datetime.datetime.now()
    date_delta = datetime.timedelta(days=int(num_days))
    date_ago = date_today - date_delta
    return date_ago

## } MODULE
