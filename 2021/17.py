
def solve(targetx, targety):
    global_maxy = 0
    count = 0
    arr = []
    for i in range(targetx[1]+1):
        for j in range(0 if targety[0] > 0 else targety[0], 200):
            x_diff = i
            y_diff = j
            x, y = 0, 0
            maxy = 0
            while y >= targety[0]:
                if y > maxy:
                    maxy = y
                if targetx[0] <= x <= targetx[1] and (targety[0] <= y <= targety[1]):
                    count += 1
                    arr.append((i, j))
                    if maxy > global_maxy:
                        global_maxy = maxy
                    break
                x += x_diff
                y += y_diff
                if x_diff > 0:
                    x_diff -= 1
                elif x_diff < 0:
                    x_diff += 1
                y_diff -= 1

    return global_maxy, count


def run():
    with open('input') as file:
        line = file.readline().strip()[13:].split(', ')
        targetx = tuple(map(int, line[0][2:].split('..')))
        targety = tuple(map(int, line[1][2:].split('..')))
        print(solve(targetx, targety))



run()
