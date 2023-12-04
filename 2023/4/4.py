import sys

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def main(filename):
    points = 0
    lines = read_lines(filename)
    cards = [1]*len(lines)
    for i,line in enumerate(lines):
        winning, current = line.split(":")[1].split("|")
        winning = list(map(lambda x: int(x), filter(lambda y: y!='', winning.strip().split(" "))))
        current = list(map(lambda x: int(x), filter(lambda y: y!='', current.strip().split(" "))))
        winning = set(winning)
        w = 0
        for n in current:
            if n in winning:
                w += 1
        # points calculation
        if w > 0:
            if w == 1:
                points += 1
            else:
                points += 2**(w-1)
        # cards calculation
        for j in range(i+1, i+w+1):
            if j < len(cards):
                cards[j] += cards[i]
        
    print("PART-1", points)
    print("PART-2", sum(cards))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('4.small.input')
        print('-'*10)
        print('Large:')
        main('4.input')
    else:
        main(sys.argv[1])
