#!/usr/bin/env python

import re

pairs = [tuple(map(int, p)) for p in re.findall(r"mul\((\d+),(\d+)\)", open(0).read())]

print(sum(x * y for x, y in pairs))
