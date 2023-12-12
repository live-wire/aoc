import sys
from functools import cache

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def solver(line, groups):
    @cache
    def check(pos, current_group, progress):
        if pos == len(line):
            return current_group <= 0 and progress == len(groups)
        cnt = 0
        for c in ('.', '#'):
            if line[pos] == '?' or line[pos] == c:
                if c == '.':
                    if current_group <= 0:
                        cnt += check(pos+1, -1, progress)
                else:
                    if current_group > 0:
                        cnt += check(pos+1, current_group-1, progress)
                    elif current_group < 0 and progress < len(groups):
                        cnt += check(pos+1, groups[progress]-1, progress+1)

        return cnt
    retval = check(0, -1, 0)
    check.cache_clear()
    return retval
    
def main(filename):
    part1 = 0
    part2 = 0
    for line in read_lines(filename):
        pattern, counts = line.split(' ')
        groups = list(map(int, counts.split(',')))
        part1 += solver(pattern, groups)
        pattern = "?".join([pattern] * 5)
        groups = groups * 5
        part2 += solver(pattern, groups)

    print("PART-1:", part1)
    print("PART-2:", part2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('12.small.input')
        print('-'*10)
        print('Large:')
        main('12.input')
    else:
        main(sys.argv[1])
