import sys
from collections import Counter

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]
    
face_cards = {'A':14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, 'W':1}
categories = [0, 10, 20, 30, 32, 40, 50]
joker_jumps = {0: 10, 10: 30, 20: 32, 30: 40, 32: 40, 40: 50, 50: 50}

def get_category(counts):
    jokers = counts['W'] if 'W' in counts else 0
    del counts['W']
    category = get_category_without_jokers(counts)
    for _ in range(jokers):
        category = joker_jumps[category]
    return category

def get_category_without_jokers(counts):
    vals = counts.values()
    valcounter = Counter(vals)
    if valcounter[5] == 1:
        return 50
    elif valcounter[4] == 1:
        return 40
    elif valcounter[3] == 1 and valcounter[2] == 1:
        return 32
    elif valcounter[3] == 1:
        return 30
    elif valcounter[2] == 2:
        return 20
    elif valcounter[2] == 1:
        return 10
    else:
        return 0

class Hand:
    def __init__(self, hand, category, bid):
        self.hand = hand
        self.category = category
        self.bid = bid

    def __lt__(self, other):
        if self.category == other.category:
            for i, c in enumerate([*self.hand]):
                sc = face_cards[c] if not c.isdigit() else int(c)
                oc = face_cards[other.hand[i]] if not other.hand[i].isdigit() else int(other.hand[i])
                if sc != oc:
                    return sc < oc
        return self.category < other.category

    def __str__(self):
        return f'{self.hand}'
    def __repr__(self):
        return f'{self.hand}'

def part_one(filename):
    hand_objects = []
    for line in read_lines(filename):
        hand,bid = line.split()
        counts = Counter(hand)
        category = get_category(counts)
        bid = int(bid)
        # print(hand, bid, category)
        hand_objects.append(Hand(hand, category, bid))
    hand_objects.sort()
    # print(hand_objects)
    prodsum = 0
    rank = 1
    for item in hand_objects:
        prodsum += item.bid * rank
        rank += 1
    print("PART-1:", prodsum)

def part_two(filename):
    hand_objects = []
    for line in read_lines(filename):
        hand,bid = line.split()
        hand = hand.replace('J', 'W')
        counts = Counter(hand)
        category = get_category(counts)
        # print(hand, bid, category)
        bid = int(bid)
        # print(hand, bid, category)
        hand_objects.append(Hand(hand, category, bid))
    hand_objects.sort()
    # print(hand_objects)
    prodsum = 0
    rank = 1
    for item in hand_objects:
        prodsum += item.bid * rank
        rank += 1
    print("PART-2:", prodsum)

def main(filename):
    part_one(filename)
    part_two(filename)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Small:')
        main('7.small.input')
        print('-'*10)
        print('Large:')
        main('7.input')
    else:
        main(sys.argv[1])
