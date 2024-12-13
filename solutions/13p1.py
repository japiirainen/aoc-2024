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
    machines.append(Machine(Coord(*a), Coord(*b), Coord(*g)))


def minimize_cost(machine: Machine) -> int:
    for i in range(101):
        for j in range(101):
            if (
                machine.a.x * i + machine.b.x * j == machine.goal.x
                and machine.a.y * i + machine.b.y * j == machine.goal.y
            ):
                return i * 3 + j
    return 0


print(sum(map(minimize_cost, machines)))
