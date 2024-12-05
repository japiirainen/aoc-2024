#!/usr/bin/env python

from collections import defaultdict

a, b = open(0).read().split("\n\n")

rules = defaultdict(list)
for x, y in [tuple(map(int, x.split("|"))) for x in a.splitlines()]:
    rules[x].append(y)

pages = [list(map(int, x.split(","))) for x in b.splitlines()]


def valid_update(x: int, page: list[int]) -> bool:
    return all(not any(r == p for r in rules.get(x, [x])) for p in page)


def valid_page(page: list[int]):
    for i in range(len(page)):
        if not valid_update(page[i], page[:i]):
            return False
    return True


def fix_page(page: list[int]) -> list[int]:
    def go(p: list[int], idx: int) -> list[int]:
        if idx >= len(p):
            return p

        cur = page[idx]
        rule = rules.get(cur, [cur])
        for j, x in enumerate(p[:idx]):
            for r in rule:
                if x == r:
                    cur = p[idx]
                    p[idx] = r
                    p[j] = cur

        return go(p, idx + 1)

    return go(page, 1)


print(
    sum(
        fix_page(page)[len(page) // 2]
        for page in [page for page in pages if not valid_page(page)]
    )
)
