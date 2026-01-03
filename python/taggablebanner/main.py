from pathlib import Path

from taggablebanner import mdutils
from taggablebanner import svgutils

MD_FILE = Path("README.md")
SVG_FILE = Path("banner.svg")


def run_username_check(username: str):
    registered_usernames = mdutils.get_names(MD_FILE)

    if username in registered_usernames:
        raise ValueError("username already on homepage")


def add_username(username: str):
    svgutils.add_name(username, MD_FILE)
    mdutils.add_name(username, SVG_FILE)
