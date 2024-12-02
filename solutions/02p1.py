#!/usr/bin/env python

print(
    sum(
        1
        for report in (
            list(map(int, line.split())) for line in open(0).read().splitlines()
        )
        if (sorted(report) == report or sorted(report, reverse=True) == report)
        and all(
            abs(b - a) >= 1 and abs(b - a) <= 3
            for a, b in zip(sorted(report), sorted(report)[1:])
        )
    )
)
