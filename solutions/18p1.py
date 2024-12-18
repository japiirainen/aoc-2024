#!/usr/bin/env python

from collections import deque

R = 71
C = 71

bts = deque(
    [tuple([int(x) for x in line.split(",")]) for line in open(0).read().splitlines()]
)

grid = [["." for _ in range(C)] for _ in range(R)]


def way(grid):
    r = c = 0

    seen = {(r, c)}
    q = deque([(r, c, 0)])

    while q:
        r, c, steps = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < R and 0 <= nc < C and (nr, nc)):
                continue
            if grid[nr][nc] == "#":
                continue
            if (nr, nc) in seen:
                continue
            if (nr, nc) == (R - 1, C - 1):
                return steps + 1
            seen.add((nr, nc))
            q.append((nr, nc, steps + 1))
    return None


for _ in range(1024):
    br, bc = bts.popleft()
    grid[br][bc] = "#"

print(way(grid))
