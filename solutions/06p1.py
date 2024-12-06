#!/usr/bin/env python

grid = [list(line) for line in open(0).read().splitlines()]

(r, c) = next(
    (r, c)
    for r in range(len(grid))
    for c in range(len(grid[r]))
    if grid[r][c] in "><^v"
)

moves = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

seen = set()

dir = grid[r][c]


def next_dir(d: str) -> str:
    keys = list(moves.keys())
    return keys[(keys.index(d) + 1) % len(keys)]


while True:
    seen.add((r, c))
    nr, nc = r + moves[dir][0], c + moves[dir][1]
    if not (0 <= nr < len(grid) and 0 <= nc < len(grid[r])):
        break
    if grid[nr][nc] == "#":
        dir = next_dir(dir)
    else:
        r, c = nr, nc

print(len(seen))
