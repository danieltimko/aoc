from math import sqrt


def get_borders(tiles):
    borders = {}
    for tile in tiles:
        borders[tile[0]] = []
        borders[tile[0]].append(tile[1][0])
        borders[tile[0]].append(borders[tile[0]][-1][::-1])
        borders[tile[0]].append(tile[1][-1])
        borders[tile[0]].append(borders[tile[0]][-1][::-1])
        borders[tile[0]].append(''.join([row[0] for row in tile[1]]))
        borders[tile[0]].append(borders[tile[0]][-1][::-1])
        borders[tile[0]].append(''.join([row[-1] for row in tile[1]]))
        borders[tile[0]].append(borders[tile[0]][-1][::-1])
    return borders


def get_neighbors(tiles):
    borders = get_borders(tiles)
    neighbors = {}
    for number, grid in tiles:
        neighbors[number] = set()
    for i in range(len(tiles)):
        for j in range(len(tiles)):
            if i == j:
                continue
            for border in borders[tiles[i][0]]:
                if border in borders[tiles[j][0]]:
                    neighbors[tiles[i][0]].add(tiles[j][0])
                    neighbors[tiles[j][0]].add(tiles[i][0])
                    break
    return neighbors


def task1(tiles):
    neighbors = get_neighbors(tiles)
    mul = 1
    top_left = None
    for tile in neighbors.items():
        if len(tile[1]) == 2:
            mul *= tile[0]
            top_left = tile[0]
    return mul, top_left


def pprint_tile_array(array):
    print("===")
    for row in array:
        for col in row:
            print("????" if not col else col, end=" ")
        print()
    print("===")


def get_tile(tiles, number):
    for tile in tiles:
        if tile[0] == number:
            return tile[1]


def fill_neighbors(array, used_tiles, neighbors, row=0, col=0):
    unused_neighbors = [n for n in neighbors[array[row][col]] if n not in used_tiles]
    if len(unused_neighbors) == 0:
        if row == len(array) - 1 and col == len(array) - 1:
            return True
        else:
            return fill_neighbors(array, used_tiles, neighbors, row, col + 1)
    if len(unused_neighbors) == 1:
        if col == len(array) - 1 or array[row][col + 1]:
            array[row + 1][col] = unused_neighbors[0]
            used_tiles.add(unused_neighbors[0])
            return fill_neighbors(array, used_tiles, neighbors, row + 1, 0)
        elif row == len(array) - 1 or array[row + 1][col]:
            array[row][col + 1] = unused_neighbors[0]
            used_tiles.add(unused_neighbors[0])
            return fill_neighbors(array, used_tiles, neighbors, row, col + 1)
        return False
    else:
        assert len(unused_neighbors) == 2
        used_tiles.add(unused_neighbors[0])
        used_tiles.add(unused_neighbors[1])
        if col == 0 or unused_neighbors[1] in neighbors[array[row + 1][col - 1]]:
            array[row][col + 1] = unused_neighbors[0]
            array[row + 1][col] = unused_neighbors[1]
            if fill_neighbors(array, used_tiles, neighbors, row, col + 1):
                return True
            array[row][col+1] = 0
            array[row+1][col] = 0
        if col == 0 or unused_neighbors[0] in neighbors[array[row + 1][col - 1]]:
            array[row][col + 1] = unused_neighbors[1]
            array[row + 1][col] = unused_neighbors[0]
            if fill_neighbors(array, used_tiles, neighbors, row, col + 1):
                return True
            array[row][col+1] = 0
            array[row+1][col] = 0
        used_tiles.remove(unused_neighbors[0])
        used_tiles.remove(unused_neighbors[1])
    return False


def relocate_tiles(tiles):
    array_size = int(sqrt(len(tiles)))
    neighbors = get_neighbors(tiles)
    top_left = task1(tiles)[1]

    array = [[0] * array_size for _ in range(array_size)]
    array[0][0] = top_left
    used_tiles = {array[0][0]}
    assert fill_neighbors(array, used_tiles, neighbors)

    for row in range(len(array)):
        for col in range(len(array)):
            array[row][col] = (array[row][col], get_tile(tiles, array[row][col]))
    return array


def initial_rotation(array, borders):
    for _ in range(4):
        array[0][0] = array[0][0][0], rotate_grid(array[0][0][1])
        for _ in range(2):
            array[0][0] = array[0][0][0], flip_grid(array[0][0][1])
            if array[0][0][1][-1] in borders[array[1][0][0]] and \
                    ''.join([row[-1] for row in array[0][0][1]]) in borders[array[0][1][0]]:
                return


def rotate_tiles(array, borders):
    # rotate tile on [0][0] to tiles on [0][1] and [1][0]
    initial_rotation(array, borders)

    for row in range(len(array)):
        for col in range(len(array)):
            # get rid of tile numbers
            array[row][col] = array[row][col][1]

            if row == 0 and col == 0:
                continue

            # rotate and flip every tile until its border matches with the previous tile
            good = False
            for _ in range(4):
                array[row][col] = rotate_grid(array[row][col])
                for _ in range(2):
                    array[row][col] = flip_grid(array[row][col])
                    if col == 0:
                        this_border = array[row][0][0]
                        neighbor_border = array[row-1][0][-1]
                    else:
                        this_border = ''.join(row[0] for row in array[row][col])
                        neighbor_border = ''.join([row[-1] for row in array[row][col-1]])
                    if this_border == neighbor_border:
                        good = True
                        break
                if good:
                    break
            if not good:
                return False
    return True


def construct_grid(tiles):
    borders = get_borders(tiles)
    array = relocate_tiles(tiles)
    assert rotate_tiles(array, borders)

    # remove borders
    for i in range(len(array)):
        for j in range(len(array)):
            array[i][j] = [line[1:-1] for line in array[i][j][1:-1]]

    sea = []
    camera_size = len(array[0][0])
    for row in range(camera_size * len(array)):
        sea_row = ""
        for col in range(camera_size * len(array)):
            sea_row += array[row//camera_size][col//camera_size][row%camera_size][col%camera_size]
        sea.append(sea_row)
    return sea


def rotate_grid(grid):
    # clockwise
    size = len(grid)
    new_grid = [[None] * size for _ in range(size)]
    for row in range(size):
        for col in range(size):
            new_grid[col][size - row - 1] = grid[row][col]
    return [''.join(row) for row in new_grid]


def flip_grid(grid):
    # by x axis
    size = len(grid)
    new_grid = [[None] * size for _ in range(size)]
    for row in range(size):
        for col in range(len(grid[row])):
            new_grid[row][size - col - 1] = grid[row][col]
    return [''.join(row) for row in new_grid]


def pprint_grid(grid):
    for row in grid:
        print(row)
    print()


def find_monsters(sea, monster):

    sea_size = len(sea)
    monster_width = len(monster[0])
    monster_height = len(monster)

    cnt = 0
    for row in range(sea_size - monster_height + 1):
        for col in range(sea_size - monster_width + 1):
            is_monster = True
            for i in range(monster_height):
                for j in range(monster_width):
                    if monster[i][j] == '#' and sea[row+i][col+j] != '#':
                        is_monster = False
                        break
                if not is_monster:
                    break
            if is_monster:
                cnt += 1
                for i in range(monster_height):
                    new_row = ""
                    for j in range(monster_width):
                        new_row += 'O' if monster[i][j] == '#' else sea[row+i][col+j]
                    sea[row+i] = sea[row+i][:col] + new_row + sea[row+i][col+monster_width:]

    if cnt:
        water = 0
        for row in range(sea_size):
            for col in range(sea_size):
                if sea[row][col] == '#':
                    water += 1
        return water
    return 0


def task2(tiles, monster):
    sea = construct_grid(tiles)

    # check for every rotation/flip of the image
    for _ in range(4):
        sea = rotate_grid(sea)

        result = find_monsters(sea, monster)
        if result:
            return result

        result = find_monsters(flip_grid(sea), monster)
        if result:
            return result


def run():
    with open('input') as file:
        tiles = []
        splitted = file.read().split("\n\n")
        for t in splitted:
            n = int(t.split("\n")[0].split(" ")[1][:-1])
            tile = []
            for line in t.split("\n")[1:]:
                tile.append(line)
            tiles.append((n, tile))

        monster = ["..................#.",
                   "#....##....##....###",
                   " #..#..#..#..#..#..."]
        print(task1(tiles)[0])
        print(task2(tiles, monster))


run()
