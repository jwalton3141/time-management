from datetime import date
from typing import Tuple


def dict_keys_to_lower(x: dict) -> dict:
    """
    Transform dictionary keys to all lower case.

    Primary use case is for taking the names of env varibles that
    are typically upper case in a dictionary and passing them
    as function arguments which are typically lower case kwargs.

    Parameters
    ----------
    x : dict
        Dictionary to lowercase keys of.

    Returns
    ------
    dict
        Dictionary with same values as input, but lowercased keys.
    """
    return {k.lower(): v for k, v in x.items()}


def get_date_range_vals(start: date,
                        end: date) -> Tuple[date, date, int]:
    return start, end, (end-start).days
