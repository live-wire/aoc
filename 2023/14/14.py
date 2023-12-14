import sys
from collections import Counter

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def main(filename):
    grid = []
    for line in read_lines(filename):
        grid.append([*line])
    # printgrid(grid)
    # print('-'*10)
    print("PART-1:", north_load(tilt_north(grid)))
    seen = {}
    cycle_length = None
    sofar = 0
    for c in range(1000000000):
        s = strgrid(grid)
        if s in seen:
            print("CYCLE FOUND:", seen[s], c)
            cycle_length = c - seen[s]
            break
        seen[s] = c
        grid = cycle(grid)
        sofar += 1
    if cycle_length:
        remaining_cycles = (1000000000 - sofar) % cycle_length
        for _ in range(remaining_cycles):
            grid = cycle(grid)
    print("PART-2:", north_load(grid))

def north_load(grid):
    s = 0
    r = 0
    for l in grid:
        n = Counter(l)['O']
        load = n * (len(grid)-r)
        s += load
        r += 1
    return s

def printgrid(grid):
    for l in grid:
        print(''.join(l))
    print('-'*10)
    
def strgrid(grid):
    ret = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                ret.append((0,i,j))
            elif grid[i][j] == '#':
                ret.append((1,i,j))
    return tuple(ret)

def tilt_vec(vec):
    ret = vec[:]
    anchor = -1
    balls = 0
    r = 0
    while r < len(vec):
        if vec[r] == "#":
            a = anchor + 1
            for _ in range(balls):
                ret[a] = "O"
                a += 1
            while a < r:
                ret[a] = "."
                a += 1
            anchor = r
            balls = 0
        elif vec[r] == "O":
            balls += 1
        else:
            pass
        r += 1
    a = anchor + 1
    for _ in range(balls):
        ret[a] = "O"
        a += 1
    while a < r:
        ret[a] = "."
        a += 1
    return ret

def tilt_north(grid):
    transposed = transpose(grid)
    ret = []
    for r in transposed:
        ret.append(tilt_vec(r))
    return transpose(ret)

def tilt_south(grid):
    transposed = transpose(grid)
    ret = []
    for r in transposed:
        ret.append(list(reversed(tilt_vec(list(reversed(r))))))
    return transpose(ret)

def tilt_west(grid):
    ret = []
    for r in grid:
        ret.append(tilt_vec(r))
    return ret

def tilt_east(grid):
    ret = []
    for r in grid:
        ret.append(list(reversed(tilt_vec(list(reversed(r))))))
    return ret

def cycle(grid):
    return tilt_east(tilt_south(tilt_west(tilt_north(grid))))

def transpose(grid):
    grid_t = [["."]*len(grid) for _ in range(len(grid[0]))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid_t[j][i] = grid[i][j]
    return grid_t
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('14.small.input')
        print('-'*10)
        print('Large:')
        main('14.input')
    else:
        main(sys.argv[1])
