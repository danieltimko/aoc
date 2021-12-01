from math import inf
from sympy.ntheory.modular import crt


def get_departure(t, bus):
    return (int(t / bus)+1) * bus if t % bus else t


def task1(t, buses):
    min_t = (-1, inf)  # (bus_id, departure)
    for bus in buses:
        if bus == 'x':
            continue
        departure = get_departure(t, int(bus))
        if departure < min_t[1]:
            min_t = (int(bus), departure)
    return min_t[0] * (min_t[1] - t)


def task2(buses):
    equations = ([], [])
    for i in range(len(buses)):
        if buses[i] != 'x':
            # print(f"t is congruent with {-i % int(buses[i])} (mod {buses[i]})")
            equations[1].append(-i % int(buses[i]))
            equations[0].append(int(buses[i]))
    return crt(*equations)[0]


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip()), file.readlines()))
        t = int(lines[0])
        buses = lines[1].split(',')
        print(task1(t, buses), task2(buses))


run()
