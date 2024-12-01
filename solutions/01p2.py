#!/usr/bin/env python

from collections import Counter
import numpy as np

pairs = [list(map(int, line.split("   "))) for line in open(0).read().splitlines()]

xs, ys = np.sort(np.transpose(pairs))

counts: Counter[int] = Counter(xs)

print(sum(y * (counts.get(y) or 0) for y in ys))
