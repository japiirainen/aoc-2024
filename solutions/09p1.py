#!/usr/bin/env python

disk = []

for i, c in enumerate(open(0).read().strip()):
    x = int(c)
    if i % 2 == 0:
        disk += [(i // 2)] * x
    else:
        disk += [-1] * x

empty = [i for i, x in enumerate(disk) if x == -1]

for i in empty:
    while disk[-1] == -1:
        disk.pop()
    if len(disk) <= i:
        break
    disk[i] = disk.pop()

print(sum(i * x for i, x in enumerate(disk)))
