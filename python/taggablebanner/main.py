# tool modules
from taggablebanner import markdown
from taggablebanner import banner


def run_username_check(username: str):
    registered_usernames = markdown.get_names()

    if username in registered_usernames:
        raise ValueError("username already on homepage")


def add_username(username: str):
    markdown.add_name(username)
    banner.add_tag(username)
