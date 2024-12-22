#!/usr/bin/env python

from itertools import pairwise
from typing import Sequence

MOD = 16777216


def step(secret: int):
    secret = (secret ^ (secret * 64)) % MOD
    secret = (secret ^ (secret // 32)) % MOD
    secret = (secret ^ (secret * 2048)) % MOD
    return secret


def gen(secret: int):
    yield secret % 10
    for _ in range(2000):
        yield (secret := step(secret)) % 10


def index(prices: Sequence[int]):
    record = {}
    changes = [b - a for a, b in pairwise(prices)]
    for i in range(len(changes) - 3):
        seq = tuple(changes[i : i + 4])
        price = prices[i + 4]
        if seq in record:
            continue
        record[seq] = price
    return record


records = [index([*gen(secret)]) for secret in map(int, open(0).read().splitlines())]
keys = set().union(*(r.keys() for r in records))

print(max(sum(r.get(k, 0) for r in records) for k in keys))
