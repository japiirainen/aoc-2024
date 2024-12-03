#!/usr/bin/env python

import re
import parse


s = 0
enabled = True

for op in re.split(r"(do\(\)|don\'t\(\))", open(0).read()):
    enabled = True if op == "do()" else False if op == "don't()" else enabled
    s += sum(x * y for x, y in parse.findall(r"mul({:d},{:d})", op)) if enabled else 0

print(s)
