__all__ = [
    "DATA",
    "DOCS",
    "MODELS",
    "NOTEBOOKS",
    "REFERENCES",
    "REPO",
    "REPORTS",
]
__author__ = """whege"""
__date__ = "9/30/2022"
__doc__ = """Enter some text here, bitch"""

from os.path import dirname, exists

REPO = "\\".join(
    dirname(__file__).split('\\')[:-2]
)


def add_subdir(s: str) -> str:
    if not exists(new_path := f'{REPO}\\{s}'):
        raise ValueError(f"{s} is not a valid subdirectory")
    else:
        return new_path


DATA = add_subdir('data')
DOCS = add_subdir('docs')
MODELS = add_subdir('models')
NOTEBOOKS = add_subdir('notebooks')
REFERENCES = add_subdir('references')
REPORTS = add_subdir('reports')
