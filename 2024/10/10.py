# Author live-wire
#
# Year: 2024
# Day: 10

import sys


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(filename):
    grid = []
    trail_heads = []
    i = 0
    for line in read_lines(filename):
        grid.append(list(line))
        for j in range(len(line)):
            if line[j] == "0":
                trail_heads.append((i, j))
        i += 1

    def valid_moves(x, y):
        moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        filtered_moves = list(
            filter(
                lambda a: a[0] >= 0
                and a[0] < len(grid)
                and a[1] >= 0
                and a[1] < len(grid[0]),
                moves,
            )
        )
        return filtered_moves

    reached = {"reached": set()}

    def score(x, y):
        curr_val = grid[x][y]
        if curr_val == "9":
            reached["reached"].add((x, y))
            return 1
        score_sum = 0
        for m in valid_moves(x, y):
            if grid[m[0]][m[1]] == str(int(curr_val) + 1):
                score_sum += score(m[0], m[1])
        return score_sum

    part1, part2 = 0, 0
    for th in trail_heads:
        rating = score(th[0], th[1])
        s = len(reached["reached"])
        part1 += s
        part2 += rating
        # print("Score: ", s, "for trail head: ", th)
        reached["reached"].clear()

    print("Part1: ", part1)
    print("Part2: ", part2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("10.small.input")
        print("-" * 10)
        print("Large:")
        main("10.input")
    else:
        main(sys.argv[1])
