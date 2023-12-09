import sys
import functools

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def predict_next(history):
    diffs = history
    last_vals = [history[-1]]
    while not all([True if d == 0 else False for d in diffs]):
        diffs = [diffs[i] - diffs[i-1] for i in range(1, len(diffs))]
        last_vals.append(diffs[-1])
    # print(last_vals)
    return functools.reduce(lambda a,b: a+b, reversed(last_vals))

def predict_prev(history):
    diffs = history
    first_vals = [history[0]]
    while not all([True if d == 0 else False for d in diffs]):
        diffs = [diffs[i] - diffs[i-1] for i in range(1, len(diffs))]
        first_vals.append(diffs[0])
    # print(first_vals)
    first_vals = list(reversed(first_vals))
    prev = first_vals[0]
    for i in range(1, len(first_vals)):
        prev = first_vals[i] - prev
    return prev


def main(filename):
    histories = []
    for line in read_lines(filename):
        histories.append(list(map(lambda x: int(x), line.split())))
    part_one, part_two = 0,0
    for h in histories:
        part_one += predict_next(h)
        part_two += predict_prev(h)

    print('PART-1:', part_one)
    print('PART-2:', part_two)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('9.small.input')
        print('-'*10)
        print('Large:')
        main('9.input')
    else:
        main(sys.argv[1])
