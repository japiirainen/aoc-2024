#!/usr/bin/env python

rs, ps = open(0).read().split("\n\n")

registers = {}

for line in rs.splitlines():
    r, v = line.split(": ")
    registers[r[-1]] = int(v)

assert list(registers.keys()) == ["A", "B", "C"]

program = [int(op) for op in ps.split(": ")[1].split(",")]


def combo(v: int) -> int:
    if v in [0, 1, 2, 3]:
        return v
    if v == 4:
        return registers["A"]
    if v == 5:
        return registers["B"]
    if v == 6:
        return registers["C"]
    raise ValueError(f"Unknown value for combo operand: {v}")


def literal(v: int) -> int:
    return v


def step(ip: int) -> int:
    opcode = program[ip]
    operand = program[ip + 1]

    if opcode == 0:
        numerator = registers["A"]
        denominator = 2 ** combo(operand)
        registers["A"] = numerator // denominator
        return ip + 2
    elif opcode == 1:
        registers["B"] = registers["B"] ^ literal(operand)
        return ip + 2
    elif opcode == 2:
        registers["B"] = combo(operand) % 8
        return ip + 2
    elif opcode == 3:
        if registers["A"] == 0:
            return ip + 2
        return literal(operand)
    elif opcode == 4:
        registers["B"] = registers["B"] ^ registers["C"]
        return ip + 2
    elif opcode == 5:
        v = combo(operand) % 8
        out.append(str(v))
        return ip + 2
    elif opcode == 6:
        numerator = registers["A"]
        denominator = 2 ** combo(operand)
        registers["B"] = numerator // denominator
        return ip + 2
    elif opcode == 7:
        numerator = registers["A"]
        denominator = 2 ** combo(operand)
        registers["C"] = numerator // denominator
        return ip + 2

    raise ValueError(f"Unknown opcode: {opcode}")


ip = 0

out = []

while ip < len(program):
    ip = step(ip)

print(",".join(out))
