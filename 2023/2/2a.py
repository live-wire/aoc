import sys
import re
def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def main(filename):
    games = {}
    i = 1
    for line in read_lines(filename):
        games[i] = {}
        for turn in line.split(";"):
            for item in turn.split(","):
                regex = r'(\d+)(\s)([a-zA-Z]+)'
                m = re.search(regex, item)
                if not m:
                    raise Exception(f'Could not parse {item}')
                else:
                    val = int(m.group(1))
                    color = m.group(3)
                    if color not in games[i]:
                        games[i][color] = val
                    games[i][color] = max(games[i][color], val)
                    # print(f'{i}: {val} {color}')
            # print("---")
        i += 1
    
    not_more_than = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    s = 0
    power_sum = 0
    for i in games:
        if games[i]['red'] <= not_more_than['red'] and games[i]['green'] <= not_more_than['green'] and games[i]['blue'] <= not_more_than['blue']:
            s += i
        power = games[i]['red'] * games[i]['green'] * games[i]['blue']
        power_sum += power

    print('PART-1', s)
    print('PART-2', power_sum)
    
            

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('2a.small.input')
        print('-'*10)
        print('Large:')
        main('2a.input')
    else:
        main(sys.argv[1])
