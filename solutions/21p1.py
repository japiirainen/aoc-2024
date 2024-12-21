#!/usr/bin/env python

from itertools import product
from collections import deque
from functools import cache

type Keypad = list[list[str | None]]

type Seqs = dict[tuple[str, str], list[str]]


def compute_seqs(keypad: Keypad) -> Seqs:
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None:
                pos[keypad[r][c]] = (r, c)

    seqs = {}

    for x in pos:
        for y in pos:
            if x == y:
                seqs[(x, y)] = ["A"]
                continue
            possibilities = []
            q = deque([(pos[x], "")])
            optimal = float("inf")
            while q:
                (r, c), moves = q.popleft()
                for nr, nc, nm in [
                    (r - 1, c, "^"),
                    (r + 1, c, "v"),
                    (r, c - 1, "<"),
                    (r, c + 1, ">"),
                ]:
                    if not (0 <= nr < len(keypad) and 0 <= nc < len(keypad[0])):
                        continue
                    if keypad[nr][nc] is None:
                        continue
                    if keypad[nr][nc] == y:
                        if optimal < len(moves) + 1:
                            break
                        optimal = len(moves) + 1
                        possibilities.append(moves + nm + "A")
                    else:
                        q.append(((nr, nc), moves + nm))
                else:
                    continue
                break
            seqs[(x, y)] = possibilities
    return seqs


@cache
def compute_length(depth: int):
    @cache
    def go(seq: str) -> int:
        if depth == 1:
            return sum(dir_lens[(x, y)] for x, y in zip("A" + seq, seq))
        length = 0
        for x, y in zip("A" + seq, seq):
            length += min(
                compute_length(depth - 1)(subseq) for subseq in dir_seqs[(x, y)]
            )
        return length

    return go


def solve(code: str, seqs: Seqs):
    options = [seqs[(x, y)] for x, y in zip("A" + code, code)]
    return ["".join(x) for x in product(*options)]


num_keypad: Keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]

num_seqs = compute_seqs(num_keypad)

dir_keypad: Keypad = [[None, "^", "A"], ["<", "v", ">"]]

dir_seqs = compute_seqs(dir_keypad)

dir_lens = {k: len(v[0]) for k, v in dir_seqs.items()}

count = 0

for code in open(0).read().splitlines():
    inputs = solve(code, num_seqs)
    length = min(map(compute_length(2), inputs))
    count += length * int(code[:-1])

print(count)
