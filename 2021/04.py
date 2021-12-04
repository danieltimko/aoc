def check_win(board):
    for row in board:
        win = True
        for col in row:
            if not col[1]:
                win = False
        if win:
            return True
    for col in range(len(board[0])):
        win = True
        for row in range(len(board)):
            if not board[row][col][1]:
                win = False
        if win:
            return True


def sum_board(board):
    sum = 0
    for row in board:
        for col in row:
            if not col[1]:
                sum += col[0]
    return sum


def print_boards(boards):
    for board in boards:
        for row in board:
            print(row)
        print('-')


def task1(numbers, boards, task):
    won_boards = set()
    for n in numbers:
        for board in range(len(boards)):
            for row in range(len(boards[board])):
                for col in range(len(boards[board][0])):
                    if boards[board][row][col][0] == n:
                        boards[board][row][col] = (boards[board][row][col][0], True)
            if board not in won_boards and check_win(boards[board]):
                if task == 1:
                    return sum_board(boards[board]) * n
                if len(won_boards) == len(boards) - 1:
                    return sum_board(boards[board]) * n
                won_boards.add(board)


def run():
    with open('input') as file:
        lines = file.readlines()
        numbers = map(int, lines[0].split(','))
        boards = []
        for line in lines[1:]:
            if line == "\n":
                boards.append([])
            else:
                arr = []
                for num in line.strip().split(' '):
                    if num != '':
                        arr.append((int(num), False))
                boards[-1].append(arr)
        print(task1(numbers, boards, 1))
        print(task1(numbers, boards, 2))


run()
