#!/usr/bin/env python

from collections import defaultdict

a, b = open(0).read().split("\n\n")

rules = defaultdict(list)
for x, y in [tuple(map(int, x.split("|"))) for x in a.splitlines()]:
    rules[x].append(y)

pages = [list(map(int, x.split(","))) for x in b.splitlines()]


def valid_update(x: int, page: list[int]) -> bool:
    rule = rules.get(x)
    if not rule:
        return True
    for x in page:
        if any(r == x for r in rule):
            return False
    return True


def valid_page(page: list[int]):
    for i in range(len(page)):
        if not valid_update(page[i], page[:i]):
            return False
    return True


print(sum(p[len(p) // 2] for p in [page for page in pages if valid_page(page)]))
