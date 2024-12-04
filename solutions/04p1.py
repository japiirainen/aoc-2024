#!/usr/bin/env python

grid = open(0).read().splitlines()

s = 0

for r in range(len(grid)):
    for c in range(len(grid)):
        if grid[r][c] != "X":
            continue
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == dc == 0:
                    continue
                if not (0 <= r + 3 * dr < len(grid) and 0 <= c + 3 * dc < len(grid[r])):
                    continue
                if (
                    grid[r + dr][c + dc] == "M"
                    and grid[r + 2 * dr][c + 2 * dc] == "A"
                    and grid[r + 3 * dr][c + 3 * dc] == "S"
                ):
                    s += 1

print(s)
