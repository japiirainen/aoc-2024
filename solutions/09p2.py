#!/usr/bin/env python

files = {}
empty = []

pos = 0
fid = 0

for i, c in enumerate(open(0).read().strip()):
    x = int(c)
    if i % 2 == 0:
        files[fid] = (pos, x)
        fid += 1
    else:
        if x != 0:
            empty.append((pos, x))
    pos += x

while fid > 0:
    fid -= 1
    pos, size = files[fid]
    for i, (start, length) in enumerate(empty):
        if start >= pos:
            empty = empty[:i]
            break
        if size <= length:
            files[fid] = (start, size)
            if size == length:
                empty.pop(i)
            else:
                empty[i] = (start + size, length - size)
            break

s = 0

for fid, (pos, size) in files.items():
    for x in range(pos, pos + size):
        s += fid * x

print(s)
