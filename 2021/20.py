
def expand_img(img, default_color):
    new_img = [[default_color for _ in range(len(img[0]) + 2)]]
    for i in range(len(img)):
        new_img.append([default_color] + [x for x in img[i]] + [default_color])
    new_img.append([default_color for _ in range(len(img[0])+2)])
    return new_img


def get_pos(img, row, col, default_color):
    if 0 <= row < len(img) and 0 <= col < len(img[0]):
        return str(img[row][col])
    return str(default_color)


def calc_index(img, row, col, default_color):
    index = ""
    for deltarow in [-1, 0, 1]:
        for deltacol in [-1, 0, 1]:
            index += get_pos(img, row+deltarow, col+deltacol, default_color)
    return int(index, 2)


def enhance(img, algorithm, steps):
    default_color = 0
    for step in range(steps):
        output_img = expand_img(img, default_color)
        for row in range(-1, len(img)+1):
            for col in range(-1, len(img[0])+1):
                index = calc_index(img, row, col, default_color)
                output_img[row+1][col+1] = algorithm[index]
        if default_color and not algorithm[511]:
            default_color = 0
        elif not default_color and algorithm[0]:
            default_color = 1
        img = output_img
    return sum(map(sum, img))


def run():
    with open('input') as file:
        alglines, imglines = file.read().split('\n\n')
        img = []
        algorithm = ""
        for line in alglines.split('\n'):
            algorithm += line.strip()
        algorithm = [int(c == '#') for c in algorithm]
        for line in imglines.split('\n'):
            img.append([int(c == '#') for c in line.strip()])

        print(enhance(img, algorithm, 2))
        print(enhance(img, algorithm, 50))


run()
