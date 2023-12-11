import sys
from collections import defaultdict

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]
    
def in_grid(grid,pos):
    i,j = pos
    if not(0<=i<len(grid) and 0<=j<len(grid[0])):
        return False
    return True

def has_down_link(grid,pos):
    if not in_grid(grid,pos):
        return False
    i,j = pos
    return grid[i][j] in ['|', 'F', '7', 'S']

def has_up_link(grid,pos):
    if not in_grid(grid,pos):
        return False
    i,j = pos
    return grid[i][j] in ['|', 'J', 'L', 'S']

def has_left_link(grid,pos):
    if not in_grid(grid,pos):
        return False
    i,j = pos
    return grid[i][j] in ['-', '7', 'J', 'S']

def has_right_link(grid,pos):
    if not in_grid(grid,pos):
        return False
    i,j = pos
    return grid[i][j] in ['-', 'F', 'L', 'S']

dd = {
    'U': ((-1, 0), has_down_link),
    'D': ((1, 0), has_up_link),
    'L': ((0, -1), has_right_link),
    'R': ((0, 1), has_left_link),
}

directions = {
    '.': [],
    'S': ['L', 'R', 'U', 'D'],
    '|': ['U', 'D'],
    '-': ['L', 'R'],
    'F': ['R', 'D'],
    '7': ['L', 'D'],
    'L': ['U', 'R'],
    'J': ['U', 'L'],
}

from_dir_mapping = {
    'U': 'D',
    'D': 'U',
    'L': 'R',
    'R': 'L',
}

class BFS:
    def __init__(self, grid):
        self.already_checked = {}
        self.grid = grid
    
    def apply(self, curr, loopset):
        to_check = [curr]
        to_check_neighbors = set()
        out_of_grid = False
        while len(to_check):
            # print(to_check, to_check_neighbors)
            curr = to_check.pop()
            if curr in self.already_checked or curr in to_check_neighbors:
                continue
            if curr in loopset:
                self.already_checked[curr] = False
                continue
            to_check_neighbors.add(curr)
            i,j = curr
            ijn = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            extend_to_check = []
            for ij in ijn:
                if not in_grid(self.grid, ij):
                    out_of_grid = True
                else:
                    if ij not in loopset:
                        extend_to_check.append(ij)
            to_check.extend(extend_to_check)
        for item in to_check_neighbors:
            if out_of_grid:
                self.already_checked[item] = False
            else:
                print(item)
                self.already_checked[item] = True

def find_loop(grid, start):
    loops_found = {
        'loops': []
    }
    work = []
    i,j = start
    potential_starts = ['L', 'R', 'U', 'D']
    for ps in potential_starts:
        dc, df = dd[ps]
        di,dj = dc
        if df(grid, (i+di, j+dj)):
            work.append(((i+di, j+dj), from_dir_mapping[ps], [start]))

    while len(work):
        curr, from_dir, sofar = work.pop()
        # print(curr, from_dir, sofar)
        if len(loops_found['loops']) > 0:
            break
        if curr == start:
            loops_found['loops'].append(sofar)
            break
        a,b = curr
        for d in directions[grid[a][b]]:
            if d == from_dir:
                continue
            dc, df = dd[d]
            di,dj = dc
            # print(d, dc, (a+di, b+dj), df)
            if df(grid, (a+di, b+dj)):
                # print('dfs')
                work.append(((a+di, b+dj), from_dir_mapping[d], sofar+[curr]))

    print("PART-1:", len(loops_found['loops'][0])//2)
    irange, jrange = (len(grid)-1,0), (len(grid[0]),0)
    loop = loops_found['loops'][0]
    loopset = set(loop)
    # printloop(grid, loop)
    rows, cols = defaultdict(set), defaultdict(set)
    for i,j in loop:
        rows[i].add(j)
        cols[j].add(i)
        irange = (min(i, irange[0]), max(i, irange[1]))
        jrange = (min(j, jrange[0]), max(j, jrange[1]))
    s = 0
    for i in range(irange[0]+1, irange[1]):
        for j in range(jrange[0]+1, jrange[1]):
            if (i,j) not in loopset:
                # print('potential',i,j)
                pipes_left, half_up_left, half_down_left = 0,0,0
                pipes_right, half_up_right, half_down_right = 0,0,0
                for c in rows[i]:
                    if c < j:
                        if grid[i][c] == '|':
                            pipes_left += 1
                        elif grid[i][c] == 'J' or grid[i][c] == 'L':
                            half_up_left += 1
                        elif grid[i][c] == 'F' or grid[i][c] == '7':
                            half_down_left += 1
                    elif c > j:
                        if grid[i][c] == '|':
                            pipes_right += 1
                        elif grid[i][c] == 'J' or grid[i][c] == 'L':
                            half_up_right += 1
                        elif grid[i][c] == 'F' or grid[i][c] == '7':
                            half_down_right += 1
                    else:
                        raise Exception('should not happen')
                m_left = min(half_up_left, half_down_left)
                pipes_left += m_left
                m_right = min(half_up_right, half_down_right)
                pipes_right += m_right
                if pipes_left %2 == 1 or pipes_right %2 == 1:
                    s += 1

    print('PART-2:', s)

    
    
    # print("PART-2:", s)

def printloop(grid, loop):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) in loop:
                print(grid[i][j], end='')
            else:
                print('.', end='')
        print()

def main(filename):
    grid = []
    start = None
    for i,line in enumerate(read_lines(filename)):
        l = line.split()[0]
        if 'S' in l:
            start = (i, l.index('S'))
        grid.append([*l])
    find_loop(grid, start)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('10.2.small.input')
        main('10.3.small.input')
        main('10.4.small.input')
        print('-'*10)
        print('Large:')
        main('10.input')
    else:
        main(sys.argv[1])
