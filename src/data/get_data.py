__all__ = ["get_data"]
__author__ = """whege"""
__date__ = "9/30/2022"
__doc__ = """Enter some text here, bitch"""

from datetime import date, datetime
import json
from os import environ
import requests

from dotenv import load_dotenv

from src.common.directories import DATA

load_dotenv()
NOW = datetime.now()
THIS_YEAR = NOW.year
THIS_MONTH = NOW.month


def _date_range(start_date: date, end_date: date) -> list[tuple[int, int]]:
    """
    Iterate
    :param start_date:
    :param end_date:
    :return:
    """
    dates = []
    month = start_date.month

    for year in range(start_date.year, end_date.year + 1):
        while month <= 12:
            dates.append((year, month))

            if (year == end_date.year) and (month == end_date.month):
                return dates
            else:
                month += 1

        month = 1

    return dates


def _query_nyt(year: int, month: int) -> dict:
    """
    Query the NYT Archive API for articles
    :param year: Year for which to query articles
    :param month: Month for which to query articles
    :return: Dict of articles
    """
    return requests.get(
        f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={environ['NYT_KEY']}"
    ).json()


def _vali_date(d: date) -> None:
    """
    Validate a date to be queried
    :param d: Year to be queried
    :return: None
    """
    if d.year > THIS_YEAR:  # Check that the year is not after the current year
        raise ValueError("Year must be in or prior to the current year.")
    elif (d.year == THIS_YEAR) and (d.month > THIS_MONTH):  # Check that month and year are not after the current date
        raise ValueError("Month cannot be after the current month if year is the current year.")


def _write_data(data, start_date: date, end_date: date) -> None:
    """
    Write data from the API to the dist
    :param data: Data to write
    :param start_date: Start date of the query range
    :param end_date: End date of the query range
    :return: None
    """
    with open(
            f'{DATA}\\raw\\nyt_data - {start_date.year}_{start_date.month}-{end_date.year}_{end_date.month}.json',
            'w'
    ) as f:
        json.dump(data, f)


def get_data(start_date: date, end_date: date) -> None:
    """

    :param start_date:
    :param end_date:
    :return:
    """
    if start_date > end_date:
        raise ValueError("End date must come after start date.")

    for d in [start_date, end_date]:  # Validate dates
        _vali_date(d)

    dates = _date_range(start_date, end_date)

    data = [_query_nyt(y, m) for y, m in dates]

    _write_data(data, start_date, end_date)
