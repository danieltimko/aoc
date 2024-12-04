from input_utils import *


def task1(matrix: list[str]):
    dirs = []
    h = len(matrix)
    w = len(matrix[0])
    for row in matrix:
        dirs.append(row)
        dirs.append(row[::-1])
    for j in range(w):
        col = "".join(matrix[i][j] for i in range(h))
        dirs.append(col)
        dirs.append(col[::-1])
    for r in range(h):
        diag = "".join(matrix[r+i][i] for i in range(h-r))
        dirs.append(diag)
        dirs.append(diag[::-1])
        diag = "".join(matrix[r+i][w-1-i] for i in range(h-r))
        dirs.append(diag)
        dirs.append(diag[::-1])
    for c in range(w):
        diag = "".join(matrix[i][c+i] for i in range(1, w-c))
        dirs.append(diag)
        dirs.append(diag[::-1])
        diag = "".join(matrix[i][c-i] for i in range(c+1))
        dirs.append(diag)
        dirs.append(diag[::-1])
    return sum(s.count("XMAS") for s in dirs)


def task2(matrix):
    h = len(matrix)
    w = len(matrix[0])
    cnt = 0
    for r in range(1, h-1):
        for c in range(1, w-1):
            if matrix[r][c] == 'A':
                diag1 = matrix[r-1][c-1] + matrix[r][c] + matrix[r+1][c+1]
                diag2 = matrix[r-1][c+1] + matrix[r][c] + matrix[r+1][c-1]
                if diag1 in ["MAS", "SAM"] and diag2 in ["MAS", "SAM"]:
                    cnt += 1
    return cnt


def run():
    matrix = read_n_lines_one_string()

    print(task1(matrix))
    print(task2(matrix))


if __name__ == "__main__":
    run()
