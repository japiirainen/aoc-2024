#!/usr/bin/env python

from collections import defaultdict
from functools import cmp_to_key

a, b = open(0).read().split("\n\n")


rules = defaultdict(int)
for x, y in [tuple(map(int, x.split("|"))) for x in a.splitlines()]:
    rules[(x, y)] = 1
    rules[(y, x)] = -1

pages = [list(map(int, x.split(","))) for x in b.splitlines()]


def valid_page(page: list[int]) -> bool:
    for i in range(len(page)):
        for j in range(i + 1, len(page)):
            if rules.get((page[i], page[j])) == -1:
                return False
    return True


print(
    sum(
        sorted(page, key=cmp_to_key(lambda x, y: rules.get((x, y), 0)))[len(page) // 2]
        for page in [page for page in pages if not valid_page(page)]
    )
)
