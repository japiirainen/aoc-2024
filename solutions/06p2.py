#!/usr/bin/env python

grid = [list(line) for line in open(0).read().splitlines()]

(r, c) = next(
    (r, c)
    for r in range(len(grid))
    for c in range(len(grid[r]))
    if grid[r][c] in "><^v"
)

moves = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}


def next_dir(d: str) -> str:
    keys = list(moves.keys())
    return keys[(keys.index(d) + 1) % len(keys)]


def loops(grid: list[list[str]], start: tuple[int, int]) -> bool:
    r, c = start
    dir = grid[r][c]
    seen = set()
    while True:
        seen.add((r, c, dir))
        nr, nc = r + moves[dir][0], c + moves[dir][1]
        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[nr])):
            return False
        if grid[nr][nc] == "#":
            dir = next_dir(dir)
        else:
            r, c = nr, nc
        if (r, c, dir) in seen:
            return True


count = 0

for i in range(len(grid)):
    for j in range(len(grid[r])):
        if grid[i][j] == ".":
            grid[i][j] = "#"
            if loops(grid, (r, c)):
                count += 1
            grid[i][j] = "."

print(count)
