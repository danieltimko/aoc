from input_utils import *
from collections import defaultdict
from functools import cmp_to_key


class Hand:
    def __init__(self, line):
        self.cards = line.split()[0]
        self.bid = int(line.split()[1])

    def compare(self, other, task):
        val = self.eval_hand(task)
        other_val = other.eval_hand(task)
        if val == other_val:
            for i in range(5):
                if self.cards[i] != other.cards[i]:
                    return self.compare_card(self.cards[i], other.cards[i], task)
        return 1 if val < other_val else -1

    def eval_hand(self, task):
        # return value: the lower = the better
        # 0 = five of a kind
        # 1 = four of a kind
        # 2 = full house
        # 3 = three of a kind
        # 4 = two pairs
        # 5 = pair
        # 6 = high card
        d = defaultdict(lambda: 0)
        for c in self.cards:
            d[c] += 1
        if 5 in d.values():
            return 0
        if 4 in d.values():
            if task == 2 and d["J"] > 0:
                return 0
            return 1
        if 3 in d.values() and 2 in d.values():
            if task == 2 and d["J"] > 0:
                return 0
            return 2
        if 3 in d.values():
            if task == 2 and d["J"] > 0:
                return 1
            return 3
        if len([v for v in d.values() if v == 2]) == 2:
            if task == 2 and d["J"] == 2:
                return 1
            if task == 2 and d["J"] == 1:
                return 2
            return 4
        if 2 in d.values():
            if task == 2 and d["J"] > 0:
                return 3
            return 5
        return 5 if task == 2 and "J" in self.cards else 6

    @staticmethod
    def compare_card(c1, c2, task):
        order = "23456789TJQKA" if task == 1 else "J23456789TQKA"
        return 1 if order.index(c1) > order.index(c2) else -1


def get_result(hands, task):
    hands.sort(key=cmp_to_key(lambda h1, h2: h1.compare(h2, task)))
    return sum((i+1) * hand.bid for i, hand in enumerate(hands))


def run():
    lines = read_n_lines_one_string()
    hands = [Hand(line) for line in lines]

    print(get_result(hands, task=1))
    print(get_result(hands, task=2))


if __name__ == "__main__":
    run()
