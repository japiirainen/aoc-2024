#!/usr/bin/env python


lhs, khs = [], []

T = lambda xs: list(zip(*xs))
H = lambda xs: [x.count("#") - 1 for x in xs]

for block in open(0).read().split("\n\n"):
    block = block.splitlines()
    if all(x == "#" for x in block[0]):
        lhs.append(H(T(block)))
    else:
        khs.append(H([x[::-1] for x in T(block)]))

print(sum(all(a + b < 6 for a, b in zip(lh, kh)) for lh in lhs for kh in khs))
