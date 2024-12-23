#!/usr/bin/env python

import sys
import networkx as nx

G = nx.Graph()

for line in open(0).read().splitlines():
    a, b = line.split("-")
    G.add_edge(a, b)

best = set()

for i in range(2, sys.maxsize):
    clique = next(nx.community.k_clique_communities(G, i), set())
    if not clique:
        break
    best = clique

print(*list(sorted(best)), sep=",")
