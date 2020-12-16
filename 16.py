
def satisfies(value, rule):
    for condition in rule:
        if condition[0] <= value <= condition[1]:
            return True
    return False


def task1(rules, tickets):
    valid_tickets = []
    invalid_values = []
    for ticket in tickets:
        b = True
        for value in ticket:
            b = False
            for rule in rules.values():
                if satisfies(value, rule):
                    b = True
                    break
            if not b:
                invalid_values.append(value)
                break
        if b:
            valid_tickets.append(ticket)
    return valid_tickets, sum(invalid_values)


def task2(rules, tickets, my_ticket):
    valid_tickets = task1(rules, tickets)[0]
    fields = [None for _ in range(len(rules))]
    possible_fields = [set(rules.keys()) for _ in range(len(rules))]
    assigned = 0
    for ticket in valid_tickets:
        for i in range(len(ticket)):
            for rule in rules.items():
                if rule[0] in possible_fields[i] and not satisfies(ticket[i], rule[1]):
                    possible_fields[i].remove(rule[0])
    while assigned < len(rules):
        for i in range(len(rules)):
            if len(possible_fields[i]) == 1:
                fields[i] = possible_fields[i].pop()
                assigned += 1
                for j in range(len(rules)):
                    if fields[i] in possible_fields[j]:
                        possible_fields[j].remove(fields[i])

    mul = 1
    for i in range(len(my_ticket)):
        if fields[i].startswith("departure"):
            mul *= my_ticket[i]
    return mul


def run():
    with open('input') as file:
        lines = file.read()
        splitted = lines.split('\n\n')
        rules = {}
        for rule in splitted[0].split('\n'):
            temp = rule.split(': ')
            rules[temp[0]] = []
            for condition in temp[1].split(' or '):
                min_val = int(condition.split('-')[0])
                max_val = int(condition.split('-')[1])
                rules[temp[0]].append((min_val, max_val))
        my_ticket = list(map(int, splitted[1].split(':\n')[1].split(',')))
        nearby_tickets = []
        for ticket in splitted[2].split('\n')[1:]:
            nearby_tickets.append(list(map(int, ticket.split(','))))

        print(task1(rules, nearby_tickets)[1], task2(rules, nearby_tickets, my_ticket))


run()
