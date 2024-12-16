#!/usr/bin/env python

import heapq as hq

grid = [list(line) for line in open(0).read().splitlines()]

R = len(grid)
C = len(grid[0])

sr, sc = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "S")
er, ec = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "E")

seen = {(sr, sc, dir) for dir in range(4)}
q = [(0, sr, sc, dir) for dir in range(4)]

while q:
    cost, r, c, dir = hq.heappop(q)
    if (r, c) == (er, ec):
        print(cost)
        break
    for ndir, (dr, dc) in enumerate([(0, 1), (1, 0), (0, -1), (-1, 0)]):
        ncost = cost + (dir != ndir) * 1000 + 1
        nr, nc = r + dr, c + dc
        if (
            0 <= nr < R
            and 0 <= nc < C
            and grid[nr][nc] != "#"
            and (nr, nc, ndir) not in seen
        ):
            seen.add((nr, nc, ndir))
            hq.heappush(q, (ncost, nr, nc, ndir))
