from input_utils import *


class File:
    def __init__(self, size):
        self.size = size


class Directory:
    def __init__(self):
        self.children = dict()

    def mkdir(self, name):
        self.children[name] = Directory()

    def touch(self, name, size):
        self.children[name] = File(size)

    def find(self, path):
        if not path:
            return self
        if len(path) == 1:
            return self.children[path[0]]
        return self.children[path[0]].find(path[1:])

    def get_size(self):
        size = 0
        for child in self.children.values():
            if isinstance(child, Directory):
                size += child.get_size()
            else:
                size += child.size
        return size

    def print_tree(self, depth=1):
        for name, child in self.children.items():
            print(f"{' ' * depth}{name}")
            if isinstance(child, Directory):
                child.print_tree(depth + 1)

    def task1(self):
        result = 0
        if (size := self.get_size()) <= 100000:
            result += size
        for child in self.children.values():
            if isinstance(child, Directory):
                result += child.task1()
        return result

    def task2(self, needed_space):
        min_dir = float('inf')
        for child in self.children.values():
            if isinstance(child, Directory):
                min_dir = min(min_dir, child.task2(needed_space))
        if min_dir == float('inf') and (size := self.get_size()) >= needed_space:
            return size
        return min_dir


def create_fs(lines):
    fs = Directory()
    cursor = []
    for line in lines:
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '/':
                    cursor = []
                elif line[2] == '..':
                    if cursor:
                        cursor.pop()
                else:
                    cursor.append(line[2])
            elif line[1] == 'ls':
                continue
        else:
            current_dir = fs.find(cursor)
            if line[0] == 'dir':
                current_dir.mkdir(line[1])
            else:
                current_dir.touch(line[1], int(line[0]))
    return fs


def run():
    lines = read_n_lines_n_strings(' ')

    fs = create_fs(lines)
    # fs.print_tree()

    print(fs.task1())
    print(fs.task2(needed_space=fs.get_size()-40000000))


if __name__ == "__main__":
    run()
