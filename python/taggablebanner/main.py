from taggablebanner import markdownmanager
from taggablebanner import bannermanager


def run_username_check(username: str):
    registered_usernames = markdownmanager.get_names()

    # TODO: enable this again
    if username in registered_usernames:
        raise ValueError("username already on homepage")


def add_username(username: str):
    markdownmanager.add_name(username)
    bannermanager.add_tag(username)
