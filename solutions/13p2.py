#!/usr/bin/env python

import re
import numpy as np


def solve(d):
    ax, ay, bx, by, gx, gy = map(int, re.findall(r"\d+", d))
    a = np.array([[ax, bx], [ay, by]])
    b = np.array([gx, gy]) + 1e13
    nx = np.linalg.solve(a, b)
    return round(3 * nx[0] + nx[1]) if all(np.abs(np.round(nx) - nx) < 1e-3) else 0


print(sum(map(solve, open(0).read().split("\n\n"))))
