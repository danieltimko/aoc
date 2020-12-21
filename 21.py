
def get_first(s):
    temp = s.pop()
    s.add(temp)
    return temp


def solve(ingredients, allergens, task):
    options = {}
    for i in range(len(ingredients)):
        for j in range(len(allergens[i])):
            if allergens[i][j] in options:
                options[allergens[i][j]] &= set(ingredients[i])
                any_resolved = True
                while any_resolved:
                    any_resolved = False
                    for x in options.items():
                        if len(x[1]) == 1:
                            resolved = get_first(x[1])
                            for y in options.items():
                                if x[0] != y[0] and resolved in y[1]:
                                    y[1].remove(resolved)
                                    any_resolved = True
            else:
                options[allergens[i][j]] = set(ingredients[i])

    if task == 2:
        return ''.join(get_first(x[1]) + ',' for x in sorted(options.items()))[:-1]

    without_ingredient = set()
    for opt in options.values():
        without_ingredient |= opt
    cnt = 0
    for i in range(len(ingredients)):
        cnt += len(set(ingredients[i]).difference(without_ingredient))
    return cnt


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip()), file.readlines()))
        ingredients = []
        allergens = []
        for line in lines:
            ingredients.append(line.split(' (')[0].split(' '))
            allergens.append(line[:-1].split('(contains ')[1].split(', '))

        print(solve(ingredients, allergens, 1))
        print(solve(ingredients, allergens, 2))


run()
