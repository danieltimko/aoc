from math import inf


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def to_list(first):
    items = []
    node = first
    while node:
        items.append(node.val)
        node = node.next
    return items


def copy_llist(old_node, new_table):
    if not old_node:
        return None, None
    new_node = Node(old_node.val)
    new_table[new_node.val] = new_node
    new_node.next = copy_llist(old_node.next, new_table)[0]
    return new_node, new_table


def add_items(first, items, table):
    prev = get_last(first) if first else None
    for item in items:
        node = Node(item)
        if prev:
            prev.next = node
        elif not first:
            first = node
        table[item] = node
        prev = node
    return first


def get_last(first):
    node = first
    while node.next:
        node = node.next
    return node


def remove_next(node):
    removed = node.next
    node.next = removed.next
    return removed


def place_after(after, new_node):
    new_node.next = after.next
    after.next = new_node


def rotate(first, last):
    temp = first.next
    first.next = None
    last.next = first
    return temp, last.next


def get_max(first):
    max_val = 0
    node = first
    while node:
        max_val = max(max_val, node.val)
        node = node.next
    return max_val


def get_min(first):
    min_val = inf
    node = first
    while node:
        min_val = min(min_val, node.val)
        node = node.next
    return min_val


def select_destination(picked_up, current_cup, min_val, max_val):
    dest = current_cup.val-1
    while dest in picked_up or dest < min_val:
        dest = max_val if dest < min_val else dest - 1
    return dest


def task1(first, table, moves=100):
    max_val, min_val = get_max(first), get_min(first)

    move = 1
    current_cup = first
    while move <= moves:
        picked_up = []
        for _ in range(3):
            if not current_cup.next:
                first = rotate(first, current_cup)[0]
            picked_up.append(remove_next(current_cup).val)

        destination_label = select_destination(picked_up, current_cup, min_val, max_val)
        destination_cup = table[destination_label]

        p = destination_cup
        for label in picked_up:
            cup = table[label]
            place_after(p, cup)
            p = cup

        current_cup = current_cup.next if current_cup.next else first
        move += 1

    last = get_last(first)
    while first.val != 1:
        first, last = rotate(first, last)
    return first, ''.join(list(map(str, to_list(first.next))))


def task2(first, table):
    max_val = get_max(first)
    first = add_items(first, range(max_val+1, 1000001), table)
    first = task1(first, table, 10000000)[0]
    return first.next.val * first.next.next.val


def run():
    with open('input') as file:
        circle = list(map(int, file.read()))
        table = {}
        first = add_items(None, circle, table)

        print(task1(*copy_llist(first, table))[1])
        print(task2(*copy_llist(first, table)))


run()
