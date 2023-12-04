import sys

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def check_neighbors(i, j, symbols):
    to_check = [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i+1, j+1), (i-1, j+1), (i+1, j-1)]
    for x,y in to_check:
        if (x,y) in symbols:
            return True
    return False

def get_neighbors(i,j,gears):
    to_check = [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i+1, j+1), (i-1, j+1), (i+1, j-1)]
    neighbors = []
    for x,y in to_check:
        if (x,y) in gears:
            neighbors.append((x,y))
    return neighbors

def main(filename):
    i = 0
    symbols = set()
    gears = set()
    for line in read_lines(filename):
        for j,c in enumerate([*line]):
            if not(c == '.' or c.isdigit()):
                symbols.add((i, j))
                if c == '*':
                    gears.add((i, j))
        i += 1
    gear_neighbors = {}
    for k in gears:
        gear_neighbors[k] = []

    i = 0
    numsum = 0
    for line in read_lines(filename):
        number = 0
        has_neighbour = False
        gears_touching_number = set()
        for j,c in enumerate([*line]):
            if c.isdigit():
                number = number*10 + int(c)
                if has_neighbour or check_neighbors(i, j, symbols):
                    has_neighbour = True
                for n in get_neighbors(i, j, gears):
                    gears_touching_number.add(n)
                
            if not c.isdigit() and number >0 or j == len(line)-1 and number > 0:
                # print(f'{i},{j} {number} {has_neighbour}')
                if has_neighbour:
                    numsum += number
                for gtn in gears_touching_number:
                    gear_neighbors[gtn].append(number)
                gears_touching_number = set()
                number = 0
                has_neighbour = False
        i += 1
    print('PART-1', numsum)
    prodsum = 0
    for k in gear_neighbors:
        l = gear_neighbors[k]
        if len(l) == 2:
            prodsum += l[0]*l[1]
    print('PART-2', prodsum)

    


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('3a.small.input')
        print('-'*10)
        print('Large:')
        main('3a.input')
    else:
        main(sys.argv[1])
