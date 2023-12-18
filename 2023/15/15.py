import sys
from collections import defaultdict, OrderedDict

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]
def hash(chrs):
    start = 0
    for c in chrs:
        start += ord(c)
        start *= 17
        start %= 256
    return start

def main(filename):
    for line in read_lines(filename):
        s = 0
        for chrs in line.strip().split(","):
            s += hash(chrs)
        print('PART-1:', s)
    boxes = defaultdict(OrderedDict)

    for line in read_lines(filename):
        for l in line.split(","):
            l = l.strip()
            if '=' in l:
                k, v = l.split('=')
                label = k.strip()
                v = int(v.strip())
                khash = hash(label)
                boxes[khash][label] = v
            else:
                label = l.split('-')[0].strip()
                khash = hash(label)
                if label in boxes[khash]:
                    del boxes[khash][label]
                    if not len(boxes[khash]):
                        del boxes[khash]
    
    s = 0
    for k,v in boxes.items():
        j = 0
        for l,pos in v.items():
            s += (k+1)*(pos)*(j+1)
            j += 1
    print('PART-2:', s)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('15.small.input')
        print('-'*10)
        print('Large:')
        main('15.input')
    else:
        main(sys.argv[1])
