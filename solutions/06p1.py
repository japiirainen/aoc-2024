#!/usr/bin/env python

grid = {
    complex(r, c): x
    for r, line in enumerate(open(0))
    for c, x in enumerate(line.strip())
}

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
