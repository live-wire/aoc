import time
import re
import itertools
import math

def fileread(file):
    p = None
    with open(file) as f:
        p = f.read().split('\n\n')
    moves, map_items = p
    map_items = [re.findall('\w+', row) for row in map_items.split('\n')]
    map_nodes = {node: dict(L=l, R=r) for node, l, r in map_items}
    return moves, map_nodes

def solve(moves, map_nodes):
  starts, ends = [{node for node in map_nodes if node[-1] == lp} for lp in 'AZ']
  counts = []
  for s in starts:
    count, curr = 0, s
    for lr in itertools.cycle(moves):
      count += 1
      curr = map_nodes[curr][lr]
      if curr in ends:
        counts.append(count)
        if s == 'AAA' and curr == 'ZZZ': part1 = count
        break

  print("PART-1:", part1)
  print("PART-2:", math.lcm(*counts))

if __name__ == '__main__':
    print(f'Small:')
    solve(*fileread("8.small.input"))
    print(f'Large:')
    solve(*fileread("8.input"))
