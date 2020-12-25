
def calculate_loop_size(pbk, initial_subject=7):
    subject = 1
    loop_size = 0
    while subject != pbk:
        subject = (subject * initial_subject) % 20201227
        loop_size += 1
    return loop_size


def transform(subject, loop_size):
    encryption_key = 1
    for i in range(loop_size):
        encryption_key = (encryption_key * subject) % 20201227
    return encryption_key


def calculate_encryption_key(card_pbk, door_pbk):
    card_loop_size = calculate_loop_size(card_pbk)
    return transform(door_pbk, card_loop_size)


def run():
    with open('input') as file:
        keys = list(map(lambda line: int(line.strip()), file.readlines()))
        card_pbk = keys[0]
        door_pbk = keys[1]

        print(calculate_encryption_key(card_pbk, door_pbk))


run()
