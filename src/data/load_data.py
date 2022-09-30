__all__ = ["load_from_disk"]
__author__ = """whege"""
__date__ = "9/30/2022"
__doc__ = """Loads article data from the disk and prepares it for feature engineering"""

from glob import iglob
import json

from src.common.directories import DATA


def _load_file(path: str) -> dict:
    """
    Load a single file from the disk
    :param path:
    :return:
    """
    with open(path, 'r') as f:
        temp = json.load(f)

    return temp


def load_from_disk() -> list[dict]:
    """
    Load all available JSON files in the data directory
    :return:
    """
    files = list(map(
        _load_file,
        iglob(f'{DATA}\\raw\\*')
    ))

    return files
