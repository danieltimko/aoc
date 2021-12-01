
translate = {
    "e": (1, 0),
    "w": (-1, 0),
    "se": (1, -1),
    "sw": (0, -1),
    "ne": (0, 1),
    "nw": (-1, 1)
}


def parse_directions(s):
    directions = []
    while s:
        if s[0] in 'we':
            directions.append(s[0])
            s = s[1:]
        else:
            directions.append(s[:2])
            s = s[2:]
    return directions


def task1(tiles):
    colors = {}

    for tile in tiles:
        x, y = 0, 0
        for step in tile:
            dx, dy = translate[step]
            x += dx
            y += dy
        colors[(x, y)] = not colors[(x, y)] if (x, y) in colors else True
    return colors, sum(colors.values())


def count_adjacent(colors, x, y):
    def get(tx, ty):
        return (tx, ty) in colors and colors[(tx, ty)]
    return get(x-1, y+1) + get(x, y+1) + get(x-1, y) + \
           get(x+1, y) + get(x, y-1) + get(x+1, y-1)


def task2(tiles, days=100):
    colors = task1(tiles)[0]

    for _ in range(days):
        new_colors = colors.copy()
        xs = list(map(lambda t: t[0], colors.keys()))
        ys = list(map(lambda t: t[1], colors.keys()))
        minx = min(xs)
        maxx = max(xs)
        miny = min(ys)
        maxy = max(ys)

        for x in range(minx-1, maxx+2):
            for y in range(miny-1, maxy+2):
                adj = count_adjacent(colors, x, y)
                if (x, y) not in colors or not colors[(x, y)]:
                    if adj == 2:
                        new_colors[(x, y)] = True
                elif adj not in [1, 2]:
                    new_colors[(x, y)] = False
        colors = new_colors

    return sum(colors.values())


def run():
    with open('input') as file:
        tiles = list(map(lambda line: parse_directions(line.strip()), file.readlines()))
        print(task1(tiles)[1])
        print(task2(tiles))


run()
