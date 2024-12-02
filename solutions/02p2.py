#!/usr/bin/env python

lines = open(0).read().splitlines()

reports = [list(map(int, line.split())) for line in lines]

safe = 0

for r in reports:
    for i in range(len(r)):
        report = r[:i] + r[i + 1 :]
        if (sorted(report) == report or sorted(report, reverse=True) == report) and all(
            abs(b - a) >= 1 and abs(b - a) <= 3
            for a, b in zip(sorted(report), sorted(report)[1:])
        ):
            safe += 1
            break


print(safe)
