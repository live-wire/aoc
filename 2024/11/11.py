# Author live-wire
#
# Year: 2024
# Day: 11

import sys
from functools import cache


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


@cache
def expand(n: int):
    if n == 0:
        return [1]
    string_num = str(n)
    if len(string_num) % 2 == 0:
        l = len(string_num) // 2
        return [int(string_num[:l]), int(string_num[l:])]
    return [n * 2024]


@cache
def calculate_num_stones(stone: int, blinks: int) -> int:
    if blinks == 0:
        return 1
    more_stones = expand(stone)
    return sum(calculate_num_stones(num, blinks - 1) for num in more_stones)


def main(filename):
    part1, part2 = 0, 0
    numbers = []
    for line in read_lines(filename):
        numbers = list(map(lambda x: int(x), line.split()))
        break
    for n in numbers:
        part1 += calculate_num_stones(n, 25)
        part2 += calculate_num_stones(n, 75)
    print("Part1: ", part1)
    print("Part2: ", part2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("11.small.input")
        print("-" * 10)
        print("Large:")
        main("11.input")
    else:
        main(sys.argv[1])
