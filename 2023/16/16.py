import sys

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

directions = {
    'r': 3,
    'l': 5,
    'u': 7,
    'd': 11,
}

reflections = {
    "/": {
        'r': ['u'],
        'l': ['d'],
        'u': ['r'],
        'd': ['l'],
    },
    "\\": {
        'r': ['d'],
        'l': ['u'],
        'u': ['l'],
        'd': ['r'],
    },
    '|': {
        'r': ['u', 'd'],
        'l': ['u', 'd'],
        'u': ['u'],
        'd': ['d'],
    },
    '-': {
        'r': ['r'],
        'l': ['l'],
        'u': ['l', 'r'],
        'd': ['l', 'r'],
    },
}

def next(x,y,d):
    if d == 'r':
        return x,y+1
    elif d == 'l':
        return x,y-1
    elif d == 'u':
        return x-1,y
    elif d == 'd':
        return x+1,y

def solve(grid, rays, debug = False):
    energy = []
    for i in range(len(grid)):
        energy.append([1]*len(grid[i]))
    rows,cols = len(grid),len(grid[0])
    # printgrid(grid)
    while len(rays):
        pos,d = rays.pop()
        x,y = pos
        while 0<=x<rows and 0<=y<cols:
            # print(x,y,d,energy[x][y],directions[d])
            if energy[x][y] != 1 and energy[x][y] % directions[d] == 0:
                break
            energy[x][y] *= directions[d]
            # lets now decide the reflections
            if grid[x][y] in reflections:
                for r in reflections[grid[x][y]][d]:
                    rays.append((next(x,y,r), r))
                break
            else:
                pass
            x,y = next(x,y,d)
    if debug:
        printgrid(grid)
        printenergy(energy)
    s = 0
    for row in energy:
        s += sum(map(lambda x: 1, filter(lambda x: x != 1, row)))
    return s

def init(filename):
    grid = []
    for line in read_lines(filename):
        grid.append([*line])
    return grid

def part_one(filename):
    grid = init(filename)
    rays = [((0,0), 'r')]
    print("PART-1:", solve(grid, rays))

def part_two(filename):
    grid = init(filename)
    solutions = {}
    for i in range(len(grid)):
        x = ((i,0), 'r')
        rays = [x]
        solved = solve(grid, rays)
        solutions[solved] = x

        x = ((i,len(grid[i])-1), 'l')
        rays = [x]
        solved = solve(grid, rays)
        solutions[solved] = x
    for i in range(len(grid[0])):
        x = ((0,i), 'd')
        rays = [x]
        solved = solve(grid, rays)
        solutions[solved] = x

        x = ((len(grid)-1,i), 'u')
        rays = [x]
        solved = solve(grid, rays)
        solutions[solved] = x
    result = max(solutions.keys())
    print("PART-2:",result, solutions[result])

def printenergy(grid):
    for row in grid:
        print(''.join(map(lambda x: "#" if x != 1 else ".", row)))

def printgrid(grid):
    for row in grid:
        print(''.join(row))

def main(filename):
    part_one(filename)
    part_two(filename)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('16.small.input')
        print('-'*10)
        print('Large:')
        main('16.input')
    else:
        main(sys.argv[1])
