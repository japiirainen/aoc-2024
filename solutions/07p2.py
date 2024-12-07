#!/usr/bin/env python

from operator import add, mul
from typing import Callable
from functools import reduce

equations = [
    (int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split())))
    for line in open(0).read().splitlines()
]

operators: list[Callable[[int, int], int]] = [
    add,
    mul,
    lambda a, b: int(str(a) + str(b)),
]

s = 0

for test, nums in equations:
    for i in range(3 ** (len(nums) - 1)):
        indices = [i // 3**j % 3 for j in range(len(nums) - 1)]
        ops = [operators[i // 3**j % 3] for j in range(len(nums) - 1)]
        if reduce(lambda acc, x: x[0](acc, x[1]), zip(ops, nums[1:]), nums[0]) == test:
            s += test
            break

print(s)
