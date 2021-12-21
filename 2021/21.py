from itertools import product


def task1(positions):
    def roll():
        n = 1
        while True:
            yield n
            n = 1 if n == 100 else n+1

    scores = [0, 0]
    rolls = 0
    gen = roll()
    while True:
        for i in range(2):
            rollsum = next(gen) + next(gen) + next(gen)
            rolls += 3
            positions[i] = (positions[i] + rollsum) % 10
            scores[i] += positions[i] + 1
            if scores[i] >= 1000:
                return rolls * min(scores)


def task2(positions):
    def get_subresult(pos1, pos2, score1, score2):
        if score1 >= 21:
            return 1, 0
        if score2 >= 21:
            return 0, 1
        if (pos1, pos2, score1, score2) in cache:
            return cache[(pos1, pos2, score1, score2)]
        n1 = 0
        n2 = 0
        for rolls in list(product([1, 2, 3], repeat=3)):
            new_pos1 = (pos1 + sum(rolls)) % 10
            # switch players every round
            subresult2, subresult1 = get_subresult(pos2, new_pos1, score2, score1+new_pos1+1)
            n1 += subresult1
            n2 += subresult2
        cache[(pos1, pos2, score1, score2)] = (n1, n2)
        return n1, n2

    cache = {}
    return max(get_subresult(positions[0], positions[1], 0, 0))


def run():
    print(task1([1, 0]))
    print(task2([1, 0]))


run()
