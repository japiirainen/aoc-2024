#!/usr/bin/env python

from collections import defaultdict
from itertools import combinations
import numpy as np
import sys

grid = open(0).read().splitlines()

antennas = defaultdict(list)

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != ".":
            antennas[grid[r][c]].append(np.array([r, c]))

antinodes = set()

for freq, nodes in antennas.items():
    for a, b in combinations(nodes, 2):
        antinodes |= {tuple(a), tuple(b)}
        for start, diff in [(a, a - b), (b, b - a)]:
            for i in range(1, sys.maxsize):
                p = start + i * diff
                if not (0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0])):
                    break
                antinodes |= {tuple(p)}

print(len(antinodes))
