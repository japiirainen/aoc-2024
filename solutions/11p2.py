#!/usr/bin/env python

from functools import cache

stones = [int(x) for x in open(0).read().split()]


@cache
def count(stone: int, n: int) -> int:
    if n == 0:
        return 1
    if stone == 0:
        return count(1, n - 1)
    s = str(stone)
    le = len(s)
    if le % 2 == 0:
        return count(int(s[: le // 2]), n - 1) + count(int(s[le // 2 :]), n - 1)
    return count(stone * 2024, n - 1)


print(sum(count(stone, 75) for stone in stones))
