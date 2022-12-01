
INPUT_FILE_PATH = "input.txt"


def read_one_number_n_lines() -> [int]:
    with open(INPUT_FILE_PATH) as f:
        return list(map(int, f.readlines()))


def read_one_string_n_lines() -> [str]:
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda line: line.strip(), f.readlines()))


def read_n_numbers_one_line(sep=',') -> [int]:
    with open(INPUT_FILE_PATH) as f:
        return list(map(int, f.readlines()[0].split(sep)))


def read_n_strings_one_line(sep=',') -> [str]:
    with open(INPUT_FILE_PATH) as f:
        return f.readlines()[0].split(sep)


def read_n_numbers_n_lines(sep=',') -> [[int]]:
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda line: list(map(int, line.split(sep))), f.readlines()))


def read_n_groups_n_lines_one_number() -> [[int]]:
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda g: list(map(int, g.strip().split('\n'))), f.read().split('\n\n')))


def read_n_groups_n_lines_n_numbers(sep=',') -> [[[int]]]:
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda g: list(map(lambda line: list(map(int, line.split(sep))),
                                           g.strip().split('\n'))),
                        f.read().split('\n\n')))
