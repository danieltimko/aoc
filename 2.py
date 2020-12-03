
def xor(a, b):
    return (a and not b) or (not a and b)


def is_valid(entry):
    min = int(entry[0].split('-')[0])
    max = int(entry[0].split('-')[1].split(' ')[0])
    letter = entry[0].split('-')[1].split(' ')[1]
    password = entry[1][1:]
    if xor(password[min-1] == letter, password[max-1] == letter):
        return True
    return False


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip().split(':')), file.readlines()))
        count = 0
        for line in lines:
            if is_valid(line):
                count += 1
        print(count)


run()
