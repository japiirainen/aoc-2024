#!/usr/bin/env python

import sys
from itertools import chain, combinations

type Formula = tuple[str, str, str]

formulas: dict[str, Formula] = {}

for line in open(0).read().split("\n\n")[1].splitlines():
    x, op, y, z = line.replace(" -> ", " ").split()
    formulas[z] = (op, x, y)


def mk_wire(char: str, n: int) -> str:
    return char + str(n).rjust(2, "0")


def verify_z(wire: str, n: int):
    if formula := formulas.get(wire):
        op, x, y = formula
        if op != "XOR":
            return False
        if n == 0:
            return sorted([x, y]) == ["x00", "y00"]
        return (
            verify_intermediate_xor(x, n)
            and verify_carry_bit(y, n)
            or verify_intermediate_xor(y, n)
            and verify_carry_bit(x, n)
        )


def verify_intermediate_xor(wire: str, n: int):
    if formula := formulas.get(wire):
        op, x, y = formula
        if op != "XOR":
            return False
        return sorted([x, y]) == [mk_wire("x", n), mk_wire("y", n)]


def verify_carry_bit(wire: str, n: int):
    if formula := formulas.get(wire):
        op, x, y = formula
        if n == 1:
            if op != "AND":
                return False
            return sorted([x, y]) == ["x00", "y00"]
        if op != "OR":
            return False
        return (
            verify_direct_carry(x, n - 1)
            and verify_recarry(y, n - 1)
            or verify_direct_carry(y, n - 1)
            and verify_recarry(x, n - 1)
        )


def verify_direct_carry(wire: str, n: int):
    if formula := formulas.get(wire):
        op, x, y = formula
        if op != "AND":
            return False
        return sorted([x, y]) == [mk_wire("x", n), mk_wire("y", n)]


def verify_recarry(wire: str, n: int):
    if formula := formulas.get(wire):
        op, x, y = formula
        if op != "AND":
            return False
        return (
            verify_intermediate_xor(x, n)
            and verify_carry_bit(y, n)
            or verify_intermediate_xor(y, n)
            and verify_carry_bit(x, n)
        )


def progress() -> int:
    for i in range(sys.maxsize):
        if not verify_z(mk_wire("z", i), i):
            return i
    raise ValueError("Unreachable")


def find_swap():
    baseline = progress()
    for x, y in combinations(formulas, 2):
        if x == y:
            continue
        formulas[x], formulas[y] = formulas[y], formulas[x]
        if progress() > baseline:
            return [x, y]
        formulas[x], formulas[y] = formulas[y], formulas[x]
    raise ValueError("No swap found")


print(*sorted(chain.from_iterable(find_swap() for _ in range(4))), sep=",")
