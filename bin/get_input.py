#!/usr/bin/env python3

import os
import requests
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser(
        prog="get_input.py",
        description="Get input for Advent of Code 2024",
    )

    parser.add_argument("--day", type=int, help="Day to get input for", required=True)

    args = parser.parse_args()

    if not (1 <= args.day <= 25):
        raise ValueError("`day` must be an integer between 1 <= `day` <= 25")

    COOKIE = os.environ.get("COOKIE")

    if not COOKIE:
        raise ValueError("Missing `COOKIE` environment variable")

    response = requests.get(
        # TODO: change the year to 2024
        url=f"https://adventofcode.com/2023/day/{args.day}/input",
        cookies={"session": COOKIE},
        headers={
            "User-Agent": "https://github.com/japiirainen/aoc-2024 by japiirainen@proton.me"
        },
    )

    if response.status_code != 200:
        raise ValueError(f"Got error response: {response.status_code}")

    with open("input.txt", "w", encoding="utf-8") as f:
        print("Writing input to file: `input.txt` in the `CWD`")
        f.write(response.text)
