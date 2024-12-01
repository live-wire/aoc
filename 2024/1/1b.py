import sys
from collections import Counter


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(filename):
    left, right = [], []
    for line in read_lines(filename):
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    right_c = Counter(right)
    dsum = 0
    for i in range(len(left)):
        dsum += left[i] * right_c[left[i]]
    print(dsum)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("1a.small.input")
        print("-" * 10)
        print("Large:")
        main("1a.input")
    else:
        main(sys.argv[1])
