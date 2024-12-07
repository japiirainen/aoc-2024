#!/usr/bin/env python

from itertools import cycle

equations = [
    (int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split())))
    for line in open(0).read().splitlines()
]


def go(nums: list[int]):
    if len(nums) == 1:
        yield nums[0]
        return
    for res, x in zip(go(nums[1:]), cycle([nums[0]])):
        yield from [res + x, res * x, int(str(res) + str(x))]


print(sum(t for t, n in equations if any(r == t for r in go(list(reversed(n))))))
