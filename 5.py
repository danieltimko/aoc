
def bin_to_dec(b):
    d = 0
    for i in range(len(b)):
        if b[i] in "BR":
            d += 2 ** (len(b) - i - 1)
    return d


def translate_seat(seat):
    row, col = seat[:7], seat[7:]
    return bin_to_dec(row) * 8 + bin_to_dec(col)


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip()), file.readlines()))
        seats = sorted([translate_seat(line) for line in lines])
        # print(seats[len(seats)-1])
        for i in range(1, len(seats)):
            if seats[i] != seats[i-1] + 1:
                print(seats[i] - 1)


run()
