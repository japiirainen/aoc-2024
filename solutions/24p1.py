#!/usr/bin/env python

from typing import Callable


a, b = open(0).read().split("\n\n")

gates: dict[str, int | None] = {
    k: int(v) for k, v in (line.split(": ") for line in a.splitlines())
}


def parse_op(op: str, target: str) -> Callable:
    x, op, y = op.split()
    if target not in gates:
        gates[target] = None

    def f(g: Callable):
        if gates[x] is None or gates[y] is None:
            return
        gates[target] = g(gates[x], gates[y])

    if op == "AND":
        return lambda: f(lambda x, y: x & y)
    elif op == "OR":
        return lambda: f(lambda x, y: x | y)
    elif op == "XOR":
        return lambda: f(lambda x, y: x ^ y)

    raise ValueError(f"Unknown {op=}")


ops = [parse_op(*line.split(" -> ")) for line in b.splitlines()]

while any(x is None for x in {v for k, v in gates.items() if k.startswith("z")}):
    for op in ops:
        op()


zs = {k: v for k, v in gates.items() if k.startswith("z")}


def sort_key(x: tuple[str, int | None]) -> int:
    return int(x[0][1:])


print(
    int("".join(map(str, dict(reversed(sorted(zs.items(), key=sort_key))).values())), 2)
)
