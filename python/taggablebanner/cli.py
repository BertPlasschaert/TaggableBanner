import argparse

from taggablebanner import main

parser = argparse.ArgumentParser(
    prog="Tagable Banner",
    description="Check if username is allowed",
)

subparsers = parser.add_subparsers(dest="action")

parser_check = subparsers.add_parser("check", help="Check if name is already used")
parser_check.add_argument("username")

parser_add = subparsers.add_parser("add", help="Add name to profile")
parser_add.add_argument("username")


args = parser.parse_args()

if args.action == "check":
    main.run_username_check(args.username)

if args.action == "add":
    print("Adding name to page")
