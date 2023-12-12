
INPUT_FILE_PATH = "input.txt"


def list_to_int(_list: list[str]) -> [int]:
    return list(map(int, _list))


def read_n_lines_one_number() -> [int]:
    with open(INPUT_FILE_PATH) as f:
        return list_to_int(f.readlines())


def read_n_lines_one_string() -> [str]:
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda line: line.strip(), f.readlines()))


def read_one_line_n_numbers(sep=',') -> [int]:
    with open(INPUT_FILE_PATH) as f:
        return list_to_int(f.readlines()[0].split(sep))


def read_one_line_n_strings(sep=',') -> [str]:
    with open(INPUT_FILE_PATH) as f:
        return f.readlines()[0].split(sep)


def read_n_lines_n_numbers(sep=',') -> [[int]]:
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda line: list_to_int(line.strip().split(sep)), f.readlines()))


def read_n_lines_n_strings(sep=',') -> [[str]]:
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda line: line.strip().split(sep), f.readlines()))


def read_n_groups_n_lines_one_number() -> [[int]]:
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda g: list_to_int(g.strip().split('\n')), f.read().split('\n\n')))


def read_n_groups_n_lines_one_string() -> [[int]]:
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda g: g.strip().split('\n'), f.read().split('\n\n')))


def read_n_groups_n_lines_n_numbers(sep=',') -> [[[int]]]:
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda g: list(map(lambda line: list_to_int(line.strip().split(sep)),
                                           g.strip().split('\n'))),
                        f.read().split('\n\n')))


def read_graph(sep=' ', weighted=False, bidirectional=True) -> dict:
    lines = read_n_lines_n_strings(sep)
    graph = dict()
    for line in lines:
        graph[line[0]].append((line[1], int(line[2])) if weighted else line[1])
        if bidirectional:
            graph[line[1]].append((line[0], int(line[2])) if weighted else line[1])
    return graph
