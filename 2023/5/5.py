import sys
import portion as P
from typing import Tuple

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
            # print(len(seeds))
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

def faster_process_using_portion(path):
    with open(path, "r") as file:
        sections = file.read().split("\n\n")

    initial_range: P.Interval = P.empty()
    seed_values = sections[0].split(":")[1].split()
    for index in range(0, len(seed_values), 2):
        start_point = int(seed_values[index])
        end_point = start_point + int(seed_values[index + 1]) - 1
        initial_range: P.Interval = initial_range | P.closed(start_point, end_point)

    translation_intervals: list[list[Tuple[P.Interval, int]]] = []
    combined_intervals: list[P.Interval] = []
    for section in sections[1:]:
        section_combined_intervals = P.empty()
        section_translation_mappings = []
        for line in section.split("\n")[1:]:
            if not line.strip():
                continue
            target_start, source_start, length = map(int, line.split())
            source_interval = P.closed(source_start, source_start + length - 1)
            section_combined_intervals = section_combined_intervals | source_interval
            section_translation_mappings.append(
                (source_interval, target_start - source_start)
            )
        translation_intervals.append(section_translation_mappings)
        combined_intervals.append(section_combined_intervals)

    final_range = initial_range
    for (combined_interval, interval_translations) in zip(
        combined_intervals, translation_intervals
    ):
        non_overlapping = final_range - combined_interval
        updated_intervals = P.empty()
        for (interval, shift) in interval_translations:
            updated_intervals = updated_intervals | shift_interval(
                final_range & interval, shift
            )
        final_range = non_overlapping | updated_intervals

    return final_range.lower


def shift_interval(interval, shift):
    def shift_bound(bound):
        return bound + shift

    return interval.apply(
        lambda x: x.replace(upper=shift_bound, lower=shift_bound)
    )

def main(filename):
    print("PART-1:", process(filename, prepare_seeds_part_1))
    # print("PART-2:", process(filename, prepare_seeds_part_2)) # TOO SLOW
    print("PART-2:", faster_process_using_portion(filename))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('5.small.input')
        print('-'*10)
        print('Large:')
        main('5.input')
    else:
        main(sys.argv[1])
