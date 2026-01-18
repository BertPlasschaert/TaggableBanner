# Stdlib modules
from datetime import datetime

# Tool modules
from taggablebanner.const import BANNER_FILE, MD_FILE
from taggablebanner import markdown
from taggablebanner import banner


def run_username_check(username: str):
    registered_usernames = markdown.get_names()

    if username in registered_usernames:
        raise ValueError("username already on homepage")


def add_username(username: str):
    markdown.add_name(username)
    banner.add_tag(username)


def invalidate_github_cache():
    unique_string = str(datetime.now().timestamp()).split(".")[-1]
    original_name = BANNER_FILE.name
    new_name = f"banner{unique_string}{BANNER_FILE.suffix}"
    BANNER_FILE.rename(new_name)

    md_lines = list()
    with open(MD_FILE, "r") as f:
        md_lines = f.readlines()

    for index, line in enumerate(md_lines):
        if original_name in line:
            md_lines[index] = line.replace(original_name, new_name)
            break

    with open(MD_FILE, "w") as f:
        f.writelines(md_lines)
