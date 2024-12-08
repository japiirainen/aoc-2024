#!/usr/bin/env python

from collections import defaultdict
from itertools import combinations
import numpy as np

grid = open(0).read().splitlines()

antennas = defaultdict(list)

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != ".":
            antennas[grid[r][c]].append(np.array([r, c]))

antinodes = set()

for freq, nodes in antennas.items():
    for a, b in combinations(nodes, 2):
        for start, diff in [(a, a - b), (b, b - a)]:
            p = start + diff
            if not (0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0])):
                continue
            antinodes |= {tuple(p)}

print(len(antinodes))
