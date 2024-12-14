#!/usr/bin/env python

import re
import math

lines = open(0).read().splitlines()

R = 103
C = 101

robots = [tuple(map(int, re.findall(r"-?\d+", line))) for line in lines]


def safety_factor(second: int) -> int:
    def simulate(robot: tuple[int, ...]) -> tuple[int, ...]:
        c, r, vc, vr = robot
        return ((r + vr * second) % R, (c + vc * second) % C, vr, vc)

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

    return math.prod(quadrants)


print(
    min(
        ((safety_factor(second), second) for second in range(R * C)), key=lambda x: x[0]
    )[1]
)
