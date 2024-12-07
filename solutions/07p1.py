#!/usr/bin/env python


from typing import Generator


equations = [
    (int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split())))
    for line in open(0).read().splitlines()
]


def go(nums: list[int]) -> Generator[int, None, None]:
    if len(nums) == 1:
        yield nums[0]
        return
    for res in go(nums[:-1]):
        yield res * nums[-1]
        yield res + nums[-1]


print(sum(test for test, nums in equations if any(res == test for res in go(nums))))
