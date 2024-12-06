#!/usr/bin/env python

grid = {
    complex(r, c): x
    for r, line in enumerate(open(0))
    for c, x in enumerate(line.strip())
}

start = next(c for c, x in grid.items() if x == "^")


def go(grid: dict[complex, str]) -> tuple[set[complex], bool]:
    seen = set()
    pos, dir = start, -1

    while pos in grid and (pos, dir) not in seen:
        seen |= {(pos, dir)}
        if grid.get(pos + dir) == "#":
            dir *= -1j
        else:
            pos += dir

    return ({pos for pos, _ in seen}, (pos, dir) in seen)


path, *_ = go(grid)

print(sum(loops for _, loops in (go(grid | {pos: "#"}) for pos in path)))
