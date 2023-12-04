import sys

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def main(filename):
    sum_so_far = 0
    for line in read_lines(filename):
        digits = [int(i) for i in [*line] if i.isdigit()]
        sum_so_far += digits[0]*10 + digits[-1]
    print(sum_so_far)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('1a.small.input')
        print('-'*10)
        print('Large:')
        main('1a.input')
    else:
        main(sys.argv[1])
