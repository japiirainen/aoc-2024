#!/usr/bin/env python

from collections import deque

grid = [list(map(int, line)) for line in open(0).read().splitlines()]

trailheads = [(r, c) for r, row in enumerate(grid) for c, x in enumerate(row) if x == 0]


def rating(r: int, c: int) -> int:
    seen = {(r, c): 1}
    q = deque([(r, c)])
    count = 0

    while q:
        cr, cc = q.popleft()
        if grid[cr][cc] == 9:
            count += seen[(cr, cc)]
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = cr + dr, cc + dc
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                continue
            if grid[nr][nc] != grid[cr][cc] + 1:
                continue
            if (nr, nc) in seen:
                seen[(nr, nc)] += seen[(cr, cc)]
                continue
            seen[(nr, nc)] = seen[(cr, cc)]
            q.append((nr, nc))

    return count


print(sum(rating(r, c) for r, c in trailheads))
