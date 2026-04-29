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
    date_string: str,
) -> datetime.date:
    """Parse an ISO-8601 date string (`YYYY-MM-DD`) and return a `datetime.date`."""
    return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()


def cast_date_to_datetime(
    date: datetime.date,
) -> datetime.datetime:
    """Return `date` as a midnight `datetime.datetime`."""
    return datetime.datetime.combine(
        date,
        datetime.time.min,
    )


def get_date_today() -> datetime.datetime:
    """Return the current date and time."""
    return datetime.datetime.now()


def get_date_n_days_ago(
    day_count: int,
) -> datetime.datetime:
    """Return the date and time `day_count` days before now."""
    date_today = datetime.datetime.now()
    date_delta = datetime.timedelta(days=int(day_count))
    return date_today - date_delta


def get_date_n_days_before(
    end_date: datetime.datetime,
    *,
    day_count: int,
) -> datetime.datetime:
    """Return the date and time `day_count` days before `end_date`."""
    date_delta = datetime.timedelta(days=int(day_count))
    return end_date - date_delta


## } MODULE
