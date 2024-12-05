import sys
from collections import defaultdict
from functools import cmp_to_key


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(filename):
    orderings = defaultdict(set)
    updates = []
    o = True
    for line in read_lines(filename):
        if line == "":
            o = False
            continue
        if o:
            # print(line)
            l, r = line.split("|")
            l = int(l)
            r = int(r)
            orderings[r].add(l)
        else:
            line = list(map(lambda x: int(x), line.split(",")))
            updates.append(line)

    def check(up):
        upr = up
        for i in range(len(upr)):
            for j in range(i + 1, len(upr)):
                if upr[j] in orderings[upr[i]]:
                    return False
        return True

    def cmp_items(a, b):
        if a == b:
            return 0
        if b in orderings[a]:
            return 1
        else:
            return -1

    part1 = 0
    part2 = 0
    for u in updates:
        if check(u):
            part1 += u[len(u) // 2]
        else:
            uclone = u[:]
            uclone.sort(key=cmp_to_key(cmp_items))
            part2 += uclone[len(u) // 2]
    print("Part1: ", part1)
    print("Part2: ", part2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("5.small.input")
        print("-" * 10)
        print("Large:")
        main("5.input")
    else:
        main(sys.argv[1])
