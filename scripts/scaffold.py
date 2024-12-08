#!/usr/bin/env python3
#
# ./scripts/scaffold.py <year> <day>
import sys
import os


def read_template():
    with open("scripts/template.py") as f:
        return f.read()


def publish(year, day):
    template = read_template()
    update_template = template.replace("{year}", year).replace("{day}", day)
    if not os.path.exists(f"{year}/{day}"):
        os.makedirs(f"{year}/{day}")
    with open(f"{year}/{day}/{day}.py", "w") as f:
        f.write(update_template)
    with open(f"{year}/{day}/{day}.small.input", "w") as f:
        f.write("")
    with open(f"{year}/{day}/{day}.input", "w") as f:
        f.write("")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scaffold.py <year> <day>")
    else:
        publish(sys.argv[1], sys.argv[2])
