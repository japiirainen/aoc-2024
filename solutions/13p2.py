#!/usr/bin/env python

import re
from collections import namedtuple

configs = open(0).read().split("\n\n")

Coord = namedtuple("Coord", ["x", "y"])
Machine = namedtuple("Machine", ["a", "b", "goal"])

machines: list[Machine] = []

for config in configs:
    a, b, g = config.splitlines()
    a, b, g = [
        list(map(int, x)) for x in map(lambda x: re.findall(r"\d+", x), [a, b, g])
    ]
    machines.append(
        Machine(Coord(*a), Coord(*b), Coord(*[g + 10000000000000 for g in g]))
    )


def solve(machine: Machine) -> int:
    a, b, p = machine
    m = (p.x * b.y - p.y * b.x) // (a.x * b.y - a.y * b.x)
    if m * (a.x * b.y - a.y * b.x) != (p.x * b.y - p.y * b.x):
        return 0
    n = (p.y - a.y * m) // b.y
    if n * b.y != (p.y - a.y * m):
        return 0
    return 3 * m + n


print(sum(map(solve, machines)))
