# Author live-wire
#
# Year: {year}
# Day: {day}

import sys


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(filename):
    for line in read_lines(filename):
        print(line)
    part1, part2 = 0
    print("Part1: ", part1)
    print("Part2: ", part2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("{day}.small.input")
        print("-" * 10)
        print("Large:")
        main("{day}.input")
    else:
        main(sys.argv[1])
