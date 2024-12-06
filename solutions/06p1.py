#!/usr/bin/env python

grid = {r + c * 1j: l for r, l in enumerate(open(0)) for c, l in enumerate(l.strip())}

start = next(c for c, x in grid.items() if x == "^")

seen = set()

pos, dir = start, -1

while pos in grid:
    seen |= {pos}
    if grid.get(pos + dir) == "#":
        dir *= -1j
    else:
        pos += dir


print(len(seen))
