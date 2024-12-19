#!/usr/bin/env python

from functools import cache

top, bot = open(0).read().split("\n\n")

patterns = top.split(", ")
designs = bot.splitlines()


@cache
def possible(design: str) -> bool:
    if not design:
        return True

    for pattern in patterns:
        if design.startswith(pattern) and possible(design[len(pattern) :]):
            return True

    return False


print(sum(map(possible, designs)))
