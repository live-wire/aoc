# Author live-wire
#
# Year: 2024
# Day: 6

import sys


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(filename):
    grid = []
    obstacles = set()
    guard_positions = set()
    guard_now = None
    directions = ["u", "r", "d", "l"]
    curr_direction_move = {
        "u": (-1, 0),
        "r": (0, 1),
        "d": (1, 0),
        "l": (0, -1),
    }
    next_direction = lambda x: (directions.index(x) + 1) % 4
    guard_direction = "u"
    i = 0
    for line in read_lines(filename):
        l = line
        for j in range(len(l)):
            if l[j] == "^":
                guard_now = (i, j)
                guard_positions.add(guard_now)
            if l[j] == "#":
                obstacles.add((i, j))
        grid.append(l)
        i += 1
    guard_now_original = guard_now
    while 0 <= guard_now[0] < len(grid) and 0 <= guard_now[1] < len(grid[0]):
        guard_positions.add(guard_now)
        next_i, next_j = curr_direction_move[guard_direction]
        next_pos = (guard_now[0] + next_i, guard_now[1] + next_j)
        if next_pos in obstacles:
            guard_direction = directions[next_direction(guard_direction)]
            continue
        guard_now = (guard_now[0] + next_i, guard_now[1] + next_j)

    part1, part2 = len(guard_positions), 0
    print("Part1: ", part1)

    def loop_created(x, y):
        guard_now = guard_now_original
        guard_direction = "u"
        pos_so_far = set()
        while 0 <= guard_now[0] < len(grid) and 0 <= guard_now[1] < len(grid[0]):
            k = (guard_now[0], guard_now[1], guard_direction)
            if k in pos_so_far:
                return True
            pos_so_far.add(k)
            next_i, next_j = curr_direction_move[guard_direction]
            next_pos = (guard_now[0] + next_i, guard_now[1] + next_j)
            if next_pos in obstacles or next_pos == (x, y):
                guard_direction = directions[next_direction(guard_direction)]
                continue
            guard_now = (guard_now[0] + next_i, guard_now[1] + next_j)
        return False

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in obstacles:
                continue
            if (i, j) == guard_now_original:
                continue
            if loop_created(i, j):
                part2 += 1

    print("Part2: ", part2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("6.small.input")
        print("-" * 10)
        print("Large:")
        main("6.input")
    else:
        main(sys.argv[1])
