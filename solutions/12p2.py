#!/usr/bin/env python

from collections import deque

grid = [list(line) for line in open(0).read().splitlines()]

R = len(grid)
C = len(grid[0])

regions = []
seen = set()

for r in range(R):
    for c in range(C):
        if (r, c) in seen:
            continue

        seen |= {(r, c)}
        q = deque([(r, c)])
        region = {(r, c)}

        while q:
            cr, cc = q.popleft()
            for nr, nc in [(cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)]:
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if grid[cr][cc] != grid[nr][nc]:
                    continue
                if (nr, nc) in region:
                    continue
                region |= {(nr, nc)}
                q.append((nr, nc))

        regions.append(region)
        seen |= region


def sides(region: list[tuple[int, int]]) -> int:
    def f(r: float, c: float):
        return [
            (r - 0.5, c - 0.5),
            (r + 0.5, c - 0.5),
            (r + 0.5, c + 0.5),
            (r - 0.5, c + 0.5),
        ]

    candidates = {(cr, cc) for r, c in region for cr, cc in f(r, c)}

    corners = 0

    for cr, cc in candidates:
        config = [(sr, sc) in region for sr, sc in f(cr, cc)]
        n = sum(config)
        if n == 1:
            corners += 1
        elif n == 2:
            if config == [True, False, True, False] or config == [
                False,
                True,
                False,
                True,
            ]:
                corners += 2
        elif n == 3:
            corners += 1

    return corners


print(sum(len(r) * sides(r) for r in regions))
