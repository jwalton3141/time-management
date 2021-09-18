import os
from typing import List

from google.oauth2.credentials import Credentials

from . import utils
from .errors import MissingEnvVar


def get_credentials_from_dict(cred: dict) -> Credentials:
    """
    Create and return a google.oauth2.credentials.Credentials
    object from environment variables.
    """
    cred = utils.dict_keys_to_lower(cred)
    return Credentials(**cred, token_uri="https://oauth2.googleapis.com/token")


def get_credentials_from_env() -> Credentials:
    """
    Create and return a google.oauth2.credentials.Credentials
    object from environment variables.

    Expected environment variables names are
    TOKEN
    REFRESH_TOKEN
    CLIENT_ID
    CLIENT_SECRET

    Raises
    ------
    MissingEnvVar
      If not all env vars are available for authentication
    """
    args_to_search = ["TOKEN", "REFRESH_TOKEN", "CLIENT_ID", "CLIENT_SECRET"]
    if not has_env_vars(*args_to_search):
        missing = missing_env_vars(*args_to_search)
        raise MissingEnvVar(missing)

    return Credentials(
        token=os.environ["TOKEN"],
        refresh_token=os.environ["REFRESH_TOKEN"],
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        token_uri="https://oauth2.googleapis.com/token"
    )


def has_env_vars(*args) -> bool:
    """
    Checks for the presence of all env variable names given in *args

    Parameters
    ----------
    *args : *str
      names of environment variables to check for
    """
    return all([a in os.environ for a in args])


def missing_env_vars(*args) -> List[str]:
    """
    Given names of env vars to look for return a list of those which are
    missing.

    Parameters
    ----------
    *args : *str
      names of environment variables to check for
    """
    return [a for a in args if a not in os.environ]
