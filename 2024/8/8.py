# Author live-wire
#
# Year: 2024
# Day: 8

import sys
from collections import defaultdict
import itertools


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(filename):
    grid = []
    antennas = defaultdict(set)
    antinodes = set()
    antinodes2 = set()
    i = 0
    for line in read_lines(filename):
        for j in range(len(line)):
            if line[j] == ".":
                pass
            else:
                antennas[line[j]].add((i, j))
        i += 1
        grid.append(line)

    ingrid = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def process_pair(one, two, part=1):
        dx, dy = one[0] - two[0], one[1] - two[1]
        within_grid1, within_grid2 = True, True
        antinode1 = one
        antinode2 = two
        if part == 2:
            antinodes2.add(antinode1)
            antinodes2.add(antinode2)
        while within_grid1:
            antinode1 = (antinode1[0] + dx, antinode1[1] + dy)
            if ingrid(*antinode1):
                if part == 1:
                    antinodes.add(antinode1)
                antinodes2.add(antinode1)
            else:
                within_grid1 = False
            if part == 1:
                break

        while within_grid2:
            antinode2 = (antinode2[0] - dx, antinode2[1] - dy)
            if ingrid(*antinode2):
                if part == 1:
                    antinodes.add(antinode2)
                antinodes2.add(antinode2)
            else:
                within_grid2 = False
            if part == 1:
                break

    for at in antennas:
        ants = antennas[at]
        for pair in itertools.combinations(ants, 2):
            process_pair(*pair, part=1)
            process_pair(*pair, part=2)

    part1, part2 = len(antinodes), len(antinodes2)
    print("Part1: ", part1)
    print("Part2: ", part2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("8.small.input")
        print("-" * 10)
        print("Large:")
        main("8.input")
    else:
        main(sys.argv[1])
