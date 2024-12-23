#!/usr/bin/env python

from collections import defaultdict

conns = defaultdict(set)

for line in open(0).read().splitlines():
    a, b = line.split("-")
    conns[a].add(b)
    conns[b].add(a)

sets = set()

for a in conns:
    for b in conns[a]:
        for c in conns[b]:
            if a != c and a in conns[c]:
                sets.add(tuple(sorted([a, b, c])))

print(sum(any(x.startswith("t") for x in s) for s in sets))
