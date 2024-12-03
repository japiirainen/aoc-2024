#!/usr/bin/env python

import re

result = re.split(r"(do\(\)|don\'t\(\))", open(0).read())

s = 0
enabled = True

for r in result:
    if r == "do()":
        enabled = True
    elif r == "don't()":
        enabled = False
    ts = (tuple(map(int, p)) for p in re.findall(r"mul\((\d+),(\d+)\)", r))
    s += sum(x * y for x, y in ts) if enabled else 0

print(s)
