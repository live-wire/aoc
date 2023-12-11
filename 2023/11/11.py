import sys

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def print_grid(grid):
    for line in grid:
        print(''.join(line))

def get_grid(filename):
    grid = []
    galaxies = []
    rows_w_g = set()
    cols_w_g = set()
    rows_wo_g = set()
    cols_wo_g = set()
    for i,line in enumerate(read_lines(filename)):
        l = [*line]
        grid.append(l)
        for j,it in enumerate(l):
            if it == '#':
                galaxies.append((i,j))
                rows_w_g.add(i)
                cols_w_g.add(j)

    for i in range(len(grid)):
        if i not in rows_w_g:
            rows_wo_g.add(i)
    for j in range(len(grid[0])):
        if j not in cols_w_g:
            cols_wo_g.add(j)

    return grid,galaxies,rows_wo_g,cols_wo_g

def expanded_distance_sum(filename, expansion_factor=1000000):
    grid, galaxies, rows_wo_g, cols_wo_g = get_grid(filename)
    distances = {}
    for it in galaxies:
        for it2 in galaxies:
            if it == it2:
                continue
            key = tuple(sorted([it,it2]))
            if key not in distances:
                row_add, col_add = 0,0
                smaller_row, larger_row = min(it[0], it2[0]), max(it[0], it2[0])
                smaller_col, larger_col = min(it[1], it2[1]), max(it[1], it2[1])
                for r in range(smaller_row+1, larger_row):
                    if r in rows_wo_g:
                        row_add += (expansion_factor-1)
                for c in range(smaller_col+1, larger_col):
                    if c in cols_wo_g:
                        col_add += (expansion_factor-1)
                distances[key] = abs(it[0] - it2[0]) + abs(it[1] - it2[1]) + row_add + col_add
    return sum(distances.values())
    

def part_one(filename):
    print('PART-1:', expanded_distance_sum(filename, 2))

def part_two(filename):
    print('PART-2:', expanded_distance_sum(filename, 1000000))

def main(filename):
    part_one(filename)
    part_two(filename)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('11.small.input')
        print('-'*10)
        print('Large:')
        main('11.input')
    else:
        main(sys.argv[1])
