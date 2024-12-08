# Author live-wire
#
# Year: 2024
# Day: 7

import sys
import itertools


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(filename):
    part1, part2 = 0, 0

    def solve(tot, rest, characters):
        n = len(rest) - 1
        permutations = list(itertools.product(characters, repeat=n))
        for p in permutations:
            ptot = rest[0]
            for i in range(1, len(rest)):
                if p[i - 1] == "+":
                    ptot += rest[i]
                elif p[i - 1] == "*":
                    ptot *= rest[i]
                else:
                    ptot = int(str(ptot) + str(rest[i]))
            if ptot == tot:
                return True
        return False

    for line in read_lines(filename):
        tot, rest = line.split(":")
        tot = int(tot.strip())
        rest = list(map(lambda x: int(x), rest.strip().split(" ")))
        if solve(tot, rest, ["+", "*"]):
            part1 += tot
        if solve(tot, rest, ["+", "*", "|"]):
            part2 += tot
    print("Part1: ", part1)
    print("Part2: ", part2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("7.small.input")
        print("-" * 10)
        print("Large:")
        main("7.input")
    else:
        main(sys.argv[1])
