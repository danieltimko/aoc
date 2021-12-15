from collections import defaultdict


def update_counts(pairs, counts):
    new_counts = counts.copy()
    for s, count in counts.items():
        if s in pairs:
            new_counts[s] -= count
            if new_counts[s] == 0:
                new_counts.pop(s)
            new_counts[f"{s[0]}{pairs[s]}"] += count
            new_counts[f"{pairs[s]}{s[1]}"] += count
    return new_counts


def solve(arr, pairs, steps=40):
    counts = defaultdict(lambda: 0)
    for i in range(len(arr)-1):
        counts[arr[i:i+2]] += 1

    for step in range(1, steps+1):
        counts = update_counts(pairs, counts)

    chars = defaultdict(lambda: 0)
    for (c1, _), count in counts.items():
        chars[c1] += count
    chars[arr[-1]] += 1
    return max(chars.values()) - min(chars.values())


def run():
    with open('input') as file:
        lines = file.readlines()
        arr = lines[0].strip()
        pairs = {}
        for line in lines[2:]:
            a, b = line.strip().split(' -> ')
            pairs[a] = b

        print(solve(arr, pairs, 10), solve(arr, pairs, 40))


run()
