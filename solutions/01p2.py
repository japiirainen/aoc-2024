#!/usr/bin/env python

import numpy as np

pairs = [list(map(int, line.split("   "))) for line in open(0).read().splitlines()]

ls, rs = np.sort(np.transpose(pairs)).tolist()

print(sum(x * rs.count(x) for x in ls))
