#!/usr/bin/env python

import re
import math

lines = open(0).read().splitlines()

R = 103
C = 101

robots = [tuple(map(int, re.findall(r"-?\d+", line))) for line in lines]


def simulate(robot: tuple[int, ...]) -> tuple[int, ...]:
    c, r, vc, vr = robot
    return ((r + vr * 100) % R, (c + vc * 100) % C, vr, vc)


quadrants = [0] * 4

for r, c, _, _ in map(simulate, robots):
    if r < (R - 1) // 2 and c < (C - 1) // 2:
        quadrants[0] += 1
    elif r < (R - 1) // 2 and c > (C - 1) // 2:
        quadrants[1] += 1
    elif r > (R - 1) // 2 and c < (C - 1) // 2:
        quadrants[2] += 1
    elif r > (R - 1) // 2 and c > (C - 1) // 2:
        quadrants[3] += 1


print(math.prod(quadrants))
