#!/usr/bin/env python

import re
from collections import defaultdict

lines = open(0).read().splitlines()

R = 103
C = 101

robots: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)

for line in lines:
    px, py, vx, vy = map(int, re.findall(r"-?\d+", line))
    robots[(py, px)].append((vy, vx))


def image():
    img = [["." for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if (r, c) in robots:
                img[r][c] = "#"
            else:
                img[r][c] = "."
    return "\n".join("".join(row) for row in img)


def calc_togetherness(a):
    t = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != "#":
                continue
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = (i + dx, j + dy)
                if 0 <= nx < len(a) and 0 <= ny < len(a[0]) and a[nx][ny] == "#":
                    t += 1
                    break
    return t


m = 0
for i in range(10_000):
    new_robots = defaultdict(list)
    for (r, c), velocities in robots.items():
        for vr, vc in velocities:
            nr, nc = (r + vr) % R, (c + vc) % C
            new_robots[(nr, nc)].append((vr, vc))
    robots = new_robots

    t = calc_togetherness(image())
    m = max(m, t)

    if t == m:
        print("=" * 80)
        print(image())
        print(i)
