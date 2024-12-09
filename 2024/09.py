from input_utils import *


def task1(disk):
    # POV: trying to be smart before finding out that for P2 I will have to do bruteforce anyway
    i = 1
    j = len(disk) - 1
    s = disk[0] * [0]
    while i < j:
        id_ = int(j/2)
        moved = min(disk[i], disk[j])
        s += moved * [id_]
        disk[i] -= moved
        disk[j] -= moved
        if disk[i] == 0:
            s += disk[i+1] * [int((i+1)/2)]
            disk[i+1] = 0
            i += 2
        if disk[j] == 0:
            j -= 2
    for j in range(j, len(disk), 2):
        assert disk[j] == 0
    return _checksum(s)


def _checksum(d):
    return sum(i*d[i] for i in range(len(d)) if d[i] != -1)


def task2(disk):
    assert len(disk) % 2 == 1
    d = []
    for i in range(0, len(disk)):
        d += disk[i] * [int(i / 2) if i % 2 == 0 else -1]
    j = len(disk)-1
    while j:
        id_ = int(j / 2)
        i1 = _find_free(d, disk[j])
        if i1:
            i2 = d.index(id_)
            if i1 < i2:
                for k in range(disk[j]):
                    d[i1+k] = id_
                    d[i2+k] = -1
        j -= 2
    return _checksum(d)


def _find_free(d, n):
    length = 0
    for i in range(len(d)):
        if d[i] == -1:
            length += 1
            if length >= n:
                return i-length+1
        else:
            length = 0
    return 0


def run():
    disk = list(map(int, read_n_lines_one_string()[0]))
    print(task1(disk.copy()))
    print(task2(disk.copy()))


if __name__ == "__main__":
    run()
