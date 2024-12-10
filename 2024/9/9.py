# Author live-wire
#
# Year: 2024
# Day: 9

import sys

EMPTY = -1


class Disk:
    def __init__(self, disk_map):
        self.data = []
        self.pos_data = []
        block_id = 0

        for i, size in enumerate(map(int, disk_map)):
            if i % 2 == 0:
                self.pos_data.append((len(self.data), size))
                self.data += [block_id] * size
                block_id += 1
            else:
                self.data += [EMPTY] * size

        self.top_block_id = block_id

    def compact_disk_p1(self):
        result = self.data[:]

        i = 0
        j = len(result) - 1
        while i < j:
            if result[i] != EMPTY:
                i += 1
                continue
            if result[j] == EMPTY:
                j -= 1
                continue
            result[i] = result[j]
            result[j] = EMPTY
        return result

    def compact(self):
        result = self.data[:]

        block_id = self.top_block_id
        while block_id > 0:
            block_id -= 1  # Subtract 1 first

            blk_idx, blk_len = self.pos_data[block_id]
            continues_free = 0
            for i in range(blk_idx):
                if result[i] == EMPTY:
                    continues_free += 1
                else:
                    continues_free = 0

                if continues_free >= blk_len:
                    # Move block
                    for j in range(blk_len):
                        result[i - j] = block_id
                        result[blk_idx + j] = EMPTY
                    break
        return result

    @staticmethod
    def checksum(data):
        return sum(i * disk_id for i, disk_id in enumerate(data) if disk_id != EMPTY)


def read_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def main(filename):
    input_text = read_lines(filename)[0]
    disk = Disk(input_text)

    p1 = disk.checksum(disk.compact_disk_p1())
    p2 = disk.checksum(disk.compact())

    print(f"Part1: {p1}")
    print(f"Part2: {p2}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Small:")
        main("9.small.input")
        print("-" * 10)
        print("Large:")
        main("9.input")
    else:
        main(sys.argv[1])
