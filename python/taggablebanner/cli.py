# stdlib modules
import argparse

# tool modules
from taggablebanner import main

parser = argparse.ArgumentParser(prog="Taggable Banner")
subparsers = parser.add_subparsers(dest="action")

parser_check = subparsers.add_parser("check", help="Check if name is already used")
parser_check.add_argument("username")

parser_add = subparsers.add_parser("add", help="Add name to profile")
parser_add.add_argument("username")

parser_check = subparsers.add_parser(
    "fix_cache",
    help="Change the banner to an unique name to invalidate the github cache",
)


def cli():
    args = parser.parse_args()

    if args.action == "check":
        main.run_username_check(args.username)

    if args.action == "add":
        main.add_username(args.username)

    if args.action == "fix_cache":
        main.invalidate_github_cache()


if __name__ == "__main__":
    cli()
