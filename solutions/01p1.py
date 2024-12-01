#!/usr/bin/env python

import numpy as np

pairs = [list(map(int, line.split("   "))) for line in open(0).read().splitlines()]

print(np.sum(np.abs(np.diff(np.sort(np.transpose(pairs)), axis=0))))
