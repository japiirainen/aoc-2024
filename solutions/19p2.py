#!/usr/bin/env python

from functools import cache

top, bot = open(0).read().split("\n\n")

patterns = top.split(", ")
designs = bot.splitlines()


@cache
def possible(design: str) -> int:
    if not design:
        return 1

    return sum(
        possible(design.replace(pattern, "", 1))
        for pattern in patterns
        if design.startswith(pattern)
    )


print(sum(map(possible, designs)))
