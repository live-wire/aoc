import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
from trie import Trie

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

digit_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven':7,
    'eight': 8,
    'nine': 9,
}

def get_digits(line):
    digits = []
    trie = Trie()
    # add all digits to trie
    for d in digit_map:
        trie.insert(d)  
    tries = [trie]
    for c in [*line]:
        if c.isdigit():
            digits.append(int(c))
            tries = [trie]
        else:
            new_tries = [trie]
            for t in tries:
                if c in t.d:
                    if t.d[c].is_word_end:
                        digits.append(digit_map[t.d[c].words_end_here[0]])
                        tries = [trie]
                    else:
                        new_tries.append(t.d[c])
            tries = new_tries
    return digits

def main(filename):
    sum_so_far = 0
    for line in read_lines(filename):
        digits = get_digits(line)
        # print(digits)
        sum_so_far += digits[0]*10 + digits[-1]
    print(sum_so_far)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('1b.small.input')
        print('-'*10)
        print('Large:')
        main('1b.input')
    else:
        main(sys.argv[1])
