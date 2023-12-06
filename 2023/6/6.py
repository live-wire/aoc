import sys
import re

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def main(filename):
    part_one(filename)
    part_two(filename)

def part_one(filename):
    times = []
    records = []
    for line in read_lines(filename):
        if 'Time:' in line:
            times = list(map(lambda x: int(x),line.split(':')[1].split()))
        else:
            records = list(map(lambda x: int(x),line.split(':')[1].split()))
    prod = 1
    for i,time in enumerate(times):
        s = 0
        for j in range(time):
            if (time - j) * j > records[i]:
                s += 1
        prod *= s
    print("PART-1", prod)

def part_two(filename):
    time,record = None, None
    for line in read_lines(filename):
        if 'Time:' in line:
            time = int(''.join(line.split(':')[1].split()))
        else:
            record = int(''.join(line.split(':')[1].split()))
    s = 0
    for i,t in enumerate(range(time)):
        if (time - i) * t > record:
            s += 1
    print("PART-2", s)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('6.small.input')
        print('-'*10)
        print('Large:')
        main('6.input')
    else:
        main(sys.argv[1])
