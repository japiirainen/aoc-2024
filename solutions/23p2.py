#!/usr/bin/env python

from collections import defaultdict

conns = defaultdict(set)

for line in open(0).read().splitlines():
    a, b = line.split("-")
    conns[a].add(b)
    conns[b].add(a)

sets = set()


def search(node: str, req: set[str]):
    k = tuple(sorted(req))
    if k in sets:
        return
    sets.add(k)
    for n in conns[node]:
        if n in req:
            continue
        if not all(n in conns[q] for q in req):
            continue
        search(n, req | {n})


for a in conns:
    search(a, {a})

print(*list(sorted(max(sets, key=len))), sep=",")
