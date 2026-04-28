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
    """Format `date` as an ISO-8601 string (`YYYY-MM-DD`)."""
    return f"{str(date.year).zfill(4)}-{str(date.month).zfill(2)}-{str(date.day).zfill(2)}"


def cast_string_to_date(
    str_date: str,
) -> datetime.date:
    """Parse an ISO-8601 date string (`YYYY-MM-DD`) and return a `datetime.date`."""
    return datetime.datetime.strptime(str_date, "%Y-%m-%d").date()


def get_date_today() -> datetime.datetime:
    """Return the current date and time."""
    return datetime.datetime.now()


def get_date_n_days_ago(
    num_days: int,
) -> datetime.datetime:
    """Return the date and time `num_days` before now."""
    date_today = datetime.datetime.now()
    date_delta = datetime.timedelta(days=int(num_days))
    return date_today - date_delta


## } MODULE
