import sys
from typing import List

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def read_file(filename):
    with open(filename) as f:
        return f.read()

def main(filename):
    inputs = read_file(filename)
    print('PART-1:', part_one(inputs))
    print('PART-2:', part_two(inputs))

def find_reflection(lines: List[str], smudge_target: int = 0) -> int:
    for split in range(len(lines) - 1):
        smudges = 0
        for i in range(split + 1):
            if split + i + 1 >= len(lines):
                continue

            row_above = lines[split - i]
            row_below = lines[split + i + 1]
            for a, b in zip(row_above, row_below):
                if a != b:
                    smudges += 1
        if smudges == smudge_target:
            return split + 1
    return 0


def part_one(inputs: str) -> int:
    input_list = [i.splitlines() for i in inputs.split("\n\n")]

    h_total = 0
    v_total = 0
    for lines in input_list:
        transpose = []
        for i in range(len(lines[0])):
            transpose.append("".join([row[i] for row in lines]))

        h_total += find_reflection(lines)
        v_total += find_reflection(transpose)

    return v_total + 100 * h_total


def part_two(inputs: str) -> int:
    input_list = [i.splitlines() for i in inputs.split("\n\n")]

    h_total = 0
    v_total = 0
    for lines in input_list:
        transpose = []
        for i in range(len(lines[0])):
            transpose.append("".join([row[i] for row in lines]))

        h_total += find_reflection(lines, 1)
        v_total += find_reflection(transpose, 1)

    return v_total + 100 * h_total


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('13.small.input')
        print('-'*10)
        print('Large:')
        main('13.input')
    else:
        main(sys.argv[1])
