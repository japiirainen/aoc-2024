#!/usr/bin/env python

from collections import deque

grid = [list(line) for line in open(0).read().splitlines()]

R, C = len(grid), len(grid[0])

r, c = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "S")

dists = [[-1] * C for _ in range(R)]
dists[r][c] = 0

q = deque([(r, c)])

while q:
    cr, cc = q.popleft()
    for nr, nc in [(cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)]:
        if (
            not (0 <= nr < R and 0 <= nc < C)
            or grid[nr][nc] == "#"
            or dists[nr][nc] != -1
        ):
            continue
        dists[nr][nc] = dists[cr][cc] + 1
        q.append((nr, nc))

count = 0

for r in range(R):
    for c in range(C):
        if grid[r][c] == "#":
            continue

        for radius in range(2, 21):
            for dr in range(radius + 1):
                dc = radius - dr
                for nr, nc in {
                    (r + dr, c + dc),
                    (r + dr, c - dc),
                    (r - dr, c + dc),
                    (r - dr, c - dc),
                }:
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if grid[nr][nc] == "#":
                        continue
                    if dists[r][c] - dists[nr][nc] >= 100 + radius:
                        count += 1

print(count)
