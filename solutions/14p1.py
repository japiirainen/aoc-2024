#!/usr/bin/env python

import re
from collections import defaultdict
from math import prod

lines = open(0).read().splitlines()

R = 103
C = 101

robots: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)

for line in lines:
    px, py, vx, vy = map(int, re.findall(r"-?\d+", line))
    robots[(py, px)].append((vy, vx))

for _ in range(100):
    new_robots = defaultdict(list)
    for (r, c), velocities in robots.items():
        for vr, vc in velocities:
            nr, nc = (r + vr) % R, (c + vc) % C
            new_robots[(nr, nc)].append((vr, vc))
    robots = new_robots

scores = [0, 0, 0, 0]

for (r, c), rs in robots.items():
    if r < (R - 1) / 2 and c < (C - 1) / 2:
        scores[0] += len(rs)
    elif r < (R - 1) / 2 and c > (C - 1) / 2:
        scores[1] += len(rs)
    elif r > (R - 1) / 2 and c < (C - 1) / 2:
        scores[2] += len(rs)
    elif r > (R - 1) / 2 and c > (C - 1) / 2:
        scores[3] += len(rs)

print(prod(scores))
