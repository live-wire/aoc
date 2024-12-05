import sys


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(filename):
    grid = []
    for line in read_lines(filename):
        grid.append(line)
    remaining_positions = ["S", "A", "M", "X"]

    conditions = {
        "right": {
            "check": lambda i, j: j >= len(grid[i]),
            "next": lambda i, j: (i, j + 1),
        },
        "left": {
            "check": lambda i, j: j < 0,
            "next": lambda i, j: (i, j - 1),
        },
        "down": {
            "check": lambda i, j: i >= len(grid),
            "next": lambda i, j: (i + 1, j),
        },
        "up": {
            "check": lambda i, j: i < 0,
            "next": lambda i, j: (i - 1, j),
        },
        "up-right": {
            "check": lambda i, j: i < 0 or j >= len(grid[i]),
            "next": lambda i, j: (i - 1, j + 1),
        },
        "up-left": {
            "check": lambda i, j: i < 0 or j < 0,
            "next": lambda i, j: (i - 1, j - 1),
        },
        "down-right": {
            "check": lambda i, j: i >= len(grid) or j >= len(grid[i]),
            "next": lambda i, j: (i + 1, j + 1),
        },
        "down-left": {
            "check": lambda i, j: i >= len(grid) or j < 0,
            "next": lambda i, j: (i + 1, j - 1),
        },
    }

    def recurse(i, j, remaining=4, direction="right"):
        if remaining == 0:
            return True
        if conditions[direction]["check"](i, j):
            return False
        if grid[i][j] != remaining_positions[remaining - 1]:
            return False
        next_i, next_j = conditions[direction]["next"](i, j)
        return recurse(next_i, next_j, remaining - 1, direction)

    def ms_finder(i, j):
        if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
            return False
        if grid[i][j] != "A":
            return False
        mc, sc, mc2, sc2 = 0, 0, 0, 0
        # top left to bottom right diagonal
        mc = mc + 1 if grid[i - 1][j - 1] == "M" else mc
        sc = sc + 1 if grid[i - 1][j - 1] == "S" else sc
        mc = mc + 1 if grid[i + 1][j + 1] == "M" else mc
        sc = sc + 1 if grid[i + 1][j + 1] == "S" else sc
        # top right to bottom left diagonal
        mc2 = mc2 + 1 if grid[i - 1][j + 1] == "M" else mc2
        sc2 = sc2 + 1 if grid[i - 1][j + 1] == "S" else sc2
        mc2 = mc2 + 1 if grid[i + 1][j - 1] == "M" else mc2
        sc2 = sc2 + 1 if grid[i + 1][j - 1] == "S" else sc2
        return mc == 1 and sc == 1 and mc2 == 1 and sc2 == 1

    part1 = 0
    part2 = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for direction in conditions:
                if recurse(i, j, 4, direction):
                    part1 += 1
            if ms_finder(i, j):
                part2 += 1
    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("4.small.input")
        print("-" * 10)
        print("Large:")
        main("4.input")
    else:
        main(sys.argv[1])
