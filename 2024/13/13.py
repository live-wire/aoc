# Author: live-wire
#
# Year: 2024
# Day: 13

import sys
import re

COST_A = 3
COST_B = 1


def read_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def parse(lines):
    print(lines)
    result = []
    btn_a = None
    btn_b = None

    for line in lines:
        if (m := re.match(r"Button ([AB]): X\+(\d+), Y\+(\d+)", line)) is not None:
            btn = (int(m.group(2)), int(m.group(3)))
            if m.group(1) == "A":
                btn_a = btn
            else:
                btn_b = btn
        elif (m := re.match(r"Prize: X=(\d+), Y=(\d+)", line)) is not None:
            prize = (int(m.group(1)), int(m.group(2)))
            assert btn_a is not None and btn_b is not None
            result.append((btn_a, btn_b, prize))
            btn_a = btn_b = None
        else:
            assert line == "", f"unexpected line {line}"

    return result


def is_int(count):
    return count.is_integer() and count >= 0


def equation_solver(entry, offset):
    (x1, y1), (x2, y2), (xp, yp) = entry

    xp += offset
    yp += offset

    b = (y1 * xp - x1 * yp) / (x2 * y1 - x1 * y2)
    a = (xp - b * x2) / x1
    if is_int(a) and is_int(b):
        return int(a), int(b)
    return None


def main(filename):
    lines = read_lines(filename)
    data = parse(lines)

    answers = []
    for offset in (0, 10_000_000_000_000):
        answer = 0
        for a, b in filter(bool, map(lambda x: equation_solver(x, offset), data)):
            answer += a * COST_A + b * COST_B
        answers.append(answer)

    part1, part2 = answers
    print("Part1: ", part1)
    print("Part2: ", part2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("13.small.input")
        print("-" * 10)
        print("Large:")
        main("13.input")
    else:
        main(sys.argv[1])
