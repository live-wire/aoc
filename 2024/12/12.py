# Author live-wire
#
# Year: 2024
# Day: 12

import sys
from collections import defaultdict


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(filename):
    grid = []
    for line in read_lines(filename):
        grid.append(line)

    topology = defaultdict(set)
    directions = lambda a, b: [(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)]
    is_valid = lambda a, b: a >= 0 and a < len(grid) and b >= 0 and b < len(grid[0])
    done = {"done": set()}

    def flood(x, y, parent):
        v = grid[parent[0]][parent[1]]
        topology[parent].add((x, y))
        done["done"].add((x, y))
        for d in directions(x, y):
            if (
                is_valid(d[0], d[1])
                and grid[d[0]][d[1]] == v
                and d not in topology[parent]
            ):
                flood(d[0], d[1], parent)

    def perimeter(x, y):
        to_ret = 0
        everywhere = defaultdict(set)
        for item in topology[(x, y)]:
            f = 4
            # left
            if (item[0], item[1] - 1) in topology[(x, y)]:
                f -= 1
            else:
                everywhere["left"].add(item)
            # right
            if (item[0], item[1] + 1) in topology[(x, y)]:
                f -= 1
            else:
                everywhere["right"].add(item)
            # up
            if (item[0] - 1, item[1]) in topology[(x, y)]:
                f -= 1
            else:
                everywhere["up"].add(item)
            # down
            if (item[0] + 1, item[1]) in topology[(x, y)]:
                f -= 1
            else:
                everywhere["down"].add(item)
            to_ret += f
        return to_ret, everywhere

    def perimeter2(x, y):
        p, everywhere = perimeter(x, y)
        up = everywhere["up"]
        minus = 0
        for item in up:
            a, b = item[0], item[1]
            if (a, b + 1) in up:
                minus += 1
        p -= minus
        # print("minus up:", minus, up)

        down = everywhere["down"]
        minus = 0
        for item in down:
            a, b = item[0], item[1]
            if (a, b + 1) in down:
                minus += 1
        p -= minus
        # print("minus down:", minus, down)

        left = everywhere["left"]
        minus = 0
        for item in left:
            a, b = item[0], item[1]
            if (a + 1, b) in left:
                minus += 1
        p -= minus
        # print("minus left:", minus, left)

        right = everywhere["right"]
        minus = 0
        for item in right:
            a, b = item[0], item[1]
            if (a + 1, b) in right:
                minus += 1
        p -= minus
        # print("minus right:", minus, right)
        return p

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) not in done["done"]:
                flood(i, j, (i, j))
    part1, part2 = 0, 0
    for k in topology:
        p1, _ = perimeter(*k)
        p2 = perimeter2(*k)
        part1 += len(topology[k]) * p1
        part2 += len(topology[k]) * p2
    print("Part1: ", part1)
    print("Part2: ", part2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("12.small.input")
        print("-" * 10)
        print("Large:")
        main("12.input")
    else:
        main(sys.argv[1])
