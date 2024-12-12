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


def perimeter(region: list[tuple[int, int]]) -> int:
    return sum(
        1
        for r, c in region
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        if (nr, nc) not in region
    )


print(sum(len(r) * perimeter(r) for r in regions))
