

def get_binary(n):
    s = ""
    for i in range(35, -1, -1):
        if 2**i <= n:
            n -= 2**i
            s += "1"
        else:
            s += "0"
    return s


def task1(lines):

    def overwrite(n):
        s = get_binary(n)
        new_s = ""
        for i in range(len(mask)):
            new_s += mask[i] if mask[i] != 'X' else s[i]
        return int(new_s, 2)

    memory = {}
    for line in lines:
        splitted = line.split(" = ")
        if splitted[0].startswith("mask"):
            mask = splitted[1]
        elif splitted[0].startswith("mem"):
            memory[int(splitted[0].split('[')[1][:-1])] = overwrite(int(splitted[1]))
    return sum(memory.values())


def task2(lines):
    def replace(s, i, c):
        new_s = ""
        for j in range(len(s)):
            new_s += c if i == j else s[j]
        return new_s

    def overwrite(n):
        b = get_binary(n)
        new_s = ""
        for i in range(36):
            new_s += mask[i] if mask[i] != '0' else b[i]
        return new_s

    def expand_and_write(a, v, i=0):
        if i == 36:
            memory[a] = v
            return
        if a[i] == 'X':
            a = replace(a, i, '0')
            expand_and_write(a, v, i+1)
            a = replace(a, i, '1')
        expand_and_write(a, v, i+1)

    memory = {}
    for line in lines:
        splitted = line.split(" = ")
        if splitted[0].startswith("mask"):
            mask = splitted[1]
        elif splitted[0].startswith("mem"):
            expand_and_write(overwrite(int(splitted[0].split('[')[1][:-1])), int(splitted[1]))

    return sum(memory.values())


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip()), file.readlines()))
        print(task1(lines), task2(lines))


run()
