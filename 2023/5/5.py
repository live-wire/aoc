import sys

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def prepare_seeds_part_1(line):
    seeds = {}
    seed_list = list(map(lambda x: int(x), line.split(":")[1].strip().split(" ")))
    for s in seed_list:
        seeds[s] = {'seed': s}
    return seeds

def prepare_seeds_part_2(line):
    seeds = {}
    seed_ranges = list(map(lambda x: int(x), line.split(":")[1].strip().split(" ")))
    for i in range(0, len(seed_ranges), 2):
        start = seed_ranges[i]
        end = seed_ranges[i+1]
        for s in range(start, start+end):
            seeds[s] = {'seed': s}
    return seeds

def process(filename, seed_prep_func):
    seeds = {}
    src, dst = None, None
    for line in read_lines(filename):
        if line == '':
            src,dst = None, None
        if "seeds:" in line:
            seeds = seed_prep_func(line)
            print(len(seeds))
        if "-to-" in line:
            src, dst = line.split(" ")[0].split("-to-")
            # print(src,dst)
            continue
        if src is not None:
            r = list(map(lambda x: int(x), line.split(" ")))
            d,s,rl = r
            for key in seeds:
                if seeds[key][src] in range(s, s+rl):
                    i = seeds[key][src] - s
                    seeds[key][dst] = d+i
            for key in seeds:
                if src in seeds[key] and dst not in seeds[key]:
                    seeds[key][dst] = seeds[key][src]
    minloc = min(list(map(lambda x: x['location'], seeds.values())))
    return minloc

def main(filename):
    print("PART-1:", process(filename, prepare_seeds_part_1))
    print("PART-2:", process(filename, prepare_seeds_part_2)) # TOO SLOW


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('5.small.input')
        print('-'*10)
        print('Large:')
        main('5.input')
    else:
        main(sys.argv[1])
