#!/usr/bin/env python

import parse

print(sum(a * b for a, b in parse.findall(r"mul({:d},{:d})", open(0).read())))
