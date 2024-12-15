#!/usr/bin/env python

expansion = {"#": "##", "O": "[]", ".": "..", "@": "@."}

grid, moves = open(0).read().split("\n\n")

grid, moves = (
    [list("".join(expansion[char] for char in line)) for line in grid.splitlines()],
    list("".join(moves.splitlines())),
)

R = len(grid)
C = len(grid[0])

r, c = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "@")

for move in moves:
    dr, dc = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}.get(move, (0, 0))
    targets = [(r, c)]
    go = True
    for cr, cc in targets:
        nr, nc = cr + dr, cc + dc
        if (nr, nc) in targets:
            continue
        char = grid[nr][nc]
        if char == "#":
            go = False
            break
        if char == "[":
            targets.append((nr, nc))
            targets.append((nr, nc + 1))
        if char == "]":
            targets.append((nr, nc))
            targets.append((nr, nc - 1))
    if not go:
        continue
    copy = [row[:] for row in grid]
    grid[r][c] = "."
    grid[r + dr][c + dc] = "@"
    for br, bc in targets[1:]:
        grid[br][bc] = "."
    for br, bc in targets[1:]:
        grid[br + dr][bc + dc] = copy[br][bc]
    r += dr
    c += dc

print(sum(100 * r + c for r in range(R) for c in range(C) if grid[r][c] == "["))
