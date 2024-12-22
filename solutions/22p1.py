#!/usr/bin/env python

MOD = 16777216


def solve(times: int):
    def go(secret: int) -> int:
        for _ in range(times):
            secret = (secret ^ (secret * 64)) % MOD
            secret = (secret ^ (secret // 32)) % MOD
            secret = (secret ^ (secret * 2048)) % MOD
        return secret

    return go


print(sum(map(solve(2000), list(map(int, open(0).read().splitlines())))))
