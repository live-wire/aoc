import sys


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(filename):
    lineS = ""
    for line in read_lines(filename):
        lineS += line
    i = 0

    def digits_only(j):
        if j >= len(lineS):
            return 0, j
        first = ""
        second = ""
        f = True
        complete = False
        while True:
            if lineS[j].isdigit():
                if f:
                    first += lineS[j]
                else:
                    second += lineS[j]
            elif lineS[j] == ",":
                f = False
            elif lineS[j] == ")":
                complete = True
                j += 1
                break
            else:
                break
            j += 1
        if len(first) and len(second) and complete:
            return int(first) * int(second), j
        else:
            return 0, j

    part1 = 0
    part2 = 0
    enabled = True
    while i < len(lineS):
        if lineS[i : i + 4] == "mul(":
            p, j = digits_only(i + 4)
            # print("PJ", p, j)
            part1 += p
            part2 += p if enabled else 0
            i = j
        elif lineS[i : i + 4] == "do()":
            enabled = True
            i = i + 4
        elif lineS[i : i + 7] == "don't()":
            enabled = False
            i = i + 7
        else:
            # print(i, lineS[i])
            i += 1
    print("PART-1: ", part1)
    print("PART-2: ", part2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("3.small.input")
        print("-" * 10)
        print("Large:")
        main("3.input")
    else:
        main(sys.argv[1])
