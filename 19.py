import re


def regex_builder(recursive_rules, basic_rules, rule, depth=0):
    if depth == 20:
        return ""
    if rule in basic_rules:
        return basic_rules[rule]
    options = []
    for opt in recursive_rules[rule]:
        r = ""
        for nxt in opt:
            r += regex_builder(recursive_rules, basic_rules, nxt, depth + 1)
        options.append(r)
    regex = ""
    for i in range(len(options)):
        regex += options[i] + "|"
    return f"({regex[:-1]})"


def count_valid(basic_rules, recursive_rules, messages, task):
    if task == 2:
        recursive_rules[8] = [[42], [42, 8]]
        recursive_rules[11] = [[42, 31], [42, 11, 31]]
    regex = regex_builder(recursive_rules, basic_rules, 0)
    cnt = 0
    for message in messages:
        if re.match(f"^{regex}$", message):
            cnt += 1
    return cnt


def run():
    with open('input') as file:
        splitted = file.read().split('\n\n')
        basic_rules = {}
        recursive_rules = {}
        messages = splitted[1].split('\n')
        for line in splitted[0].split('\n'):
            splitted_line = line.split(": ")
            if "\"" in splitted_line[1]:
                basic_rules[int(splitted_line[0])] = splitted_line[1][1]
            else:
                conditions = []
                for condition in splitted_line[1].split(" | "):
                    conditions.append(list(map(int, condition.split(" "))))
                recursive_rules[int(splitted_line[0])] = conditions

        print(count_valid(basic_rules, recursive_rules, messages, task=1))
        print(count_valid(basic_rules, recursive_rules, messages, task=2))


run()
