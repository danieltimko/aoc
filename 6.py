
def group_count_anyone(group):
    unique_answers = set()
    for person in group.split('\n'):
        for answer in person:
            unique_answers.add(answer)
    return len(unique_answers)


def group_count_everyone(group):
    unique_answers = dict()
    for person in group.split('\n'):
        for answer in person:
            unique_answers[answer] = unique_answers.get(answer, 0) + 1
    answered_by_everyone = 0
    for count in unique_answers.values():
        if count == len(group.split('\n')):
            answered_by_everyone += 1
    return answered_by_everyone


def run():
    with open('input') as file:
        groups = file.read().split('\n\n')
        count_anyone = sum([group_count_anyone(group) for group in groups])
        count_everyone = sum([group_count_everyone(group) for group in groups])
        print(count_anyone, count_everyone)


run()
