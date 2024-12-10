#!/usr/bin/env python

from collections import deque

grid = [list(map(int, line)) for line in open(0).read().splitlines()]

trailheads = [(r, c) for r, row in enumerate(grid) for c, x in enumerate(row) if x == 0]


def score(r: int, c: int) -> int:
    seen = {(r, c)}
    q = deque([(r, c)])
    count = 0

    while q:
        cr, cc = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = cr + dr, cc + dc
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                continue
            if (nr, nc) in seen:
                continue
            if grid[nr][nc] != grid[cr][cc] + 1:
                continue
            seen |= {(nr, nc)}
            if grid[nr][nc] == 9:
                count += 1
            else:
                q.append((nr, nc))

    return count


print(sum(score(r, c) for r, c in trailheads))
