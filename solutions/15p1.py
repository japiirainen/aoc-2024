#!/usr/bin/env python


grid, moves = open(0).read().split("\n\n")

grid, moves = (
    [list(line) for line in grid.splitlines()],
    list("".join(moves.splitlines())),
)

R = len(grid)
C = len(grid[0])

r, c = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "@")

for move in moves:
    dr, dc = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}.get(move, (0, 0))
    targets = [(r, c)]
    cr, cc = r, c
    go = True
    while True:
        cr += dr
        cc += dc
        char = grid[cr][cc]
        if char == "#":
            go = False
            break
        elif char == "O":
            targets.append((cr, cc))
        elif char == ".":
            break

    if not go:
        continue

    grid[r][c] = "."
    grid[r + dr][c + dc] = "@"
    for br, bc in targets[1:]:
        grid[br + dr][bc + dc] = "O"
    r += dr
    c += dc

print(sum(100 * r + c for r in range(R) for c in range(C) if grid[r][c] == "O"))
