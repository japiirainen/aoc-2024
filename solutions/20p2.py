#!/usr/bin/env python

import networkx as nx

grid = [list(line) for line in open(0).read().splitlines()]

R, C = len(grid), len(grid[0])

G = nx.Graph()

er, ec = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "E")

for r in range(R):
    for c in range(C):
        if grid[r][c] in ".SE":
            G.add_node((r, c))

for r in range(R):
    for c in range(C):
        if grid[r][c] in ".SE":
            for dr, dc in [(0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#":
                    G.add_edge((r, c), (nr, nc))

base = dict(nx.shortest_path_length(G, (er, ec)))


def get_reachable(r: int, c: int, max_dist: int) -> list[tuple[int, int]]:
    reachable = []
    for dr in range(-max_dist, max_dist + 1):
        remaining = max_dist - abs(dr)
        for dc in range(-remaining, remaining + 1):
            if dr == dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#":
                reachable.append((nr, nc))
    return reachable


def solve(cheat_size: int) -> int:
    t = 0
    for node in G.nodes:
        r, c = node
        reachable = get_reachable(r, c, cheat_size)
        for dr, dc in reachable:
            cost = abs(r - dr) + abs(c - dc)
            saving = base[(r, c)] - (base[(dr, dc)] + cost)
            if saving >= 100:
                t += 1
    return t


print(solve(20))
