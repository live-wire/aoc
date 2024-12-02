import sys


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def main(filename):
    safecount = 0
    safecount_damp = 0
    for line in read_lines(filename):
        report = list(map(lambda x: int(x), line.split()))
        if is_safe(report):
            safecount += 1
        if is_safe_damp(report):
            safecount_damp += 1
    print("PART-1: ", safecount)
    print("PART-2: ", safecount_damp)


def is_safe(report):
    it = report[0]
    increasing = True if report[1] > it else False
    if report[1] == it:
        return False
    for i in range(1, len(report)):
        if increasing:
            if report[i] > it and report[i] < it + 4:
                pass
            else:
                return False
        else:
            if report[i] < it and report[i] > it - 4:
                pass
            else:
                return False
        it = report[i]
    return True


def is_safe_damp(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        if is_safe(report[0:i] + report[i + 1 :]):
            return True
    return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("2a.small.input")
        print("-" * 10)
        print("Large:")
        main("2a.input")
    else:
        main(sys.argv[1])
