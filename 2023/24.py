from input_utils import *

from sympy import symbols, Eq, solve
from z3 import Reals, Solver


def find_intersections(stone1, stone2):
    test_area = (200000000000000, 400000000000000)

    (x1, y1, _), (vx1, vy1, _) = stone1
    (x2, y2, _), (vx2, vy2, _) = stone2
    t, s = symbols('t s')

    eq_x = Eq(x1 + t * vx1, x2 + s * vx2)
    eq_y = Eq(y1 + t * vy1, y2 + s * vy2)

    solution = solve((eq_x, eq_y), (t, s))

    if solution:
        _t = solution[t]
        _s = solution[s]
        assert x1 + _t * vx1 == x2 + _s * vx2
        assert y1 + _t * vy1 == y2 + _s * vy2
        intersection = (x1 + _t * vx1, y1 + _t * vy1)
        if _t > 0 and _s > 0 and all(test_area[0] <= intersection[i] <= test_area[1] for i in range(2)):
            return 1
    return 0


def task1(stones):
    ans = 0
    for i in range(len(stones)):
        print(i)
        for j in range(i+1, len(stones)):
            ans += find_intersections(stones[i], stones[j])
    return ans


def task2(stones):
    (x1, y1, z1), (vx1, vy1, vz1) = stones[0]
    (x2, y2, z2), (vx2, vy2, vz2) = stones[1]
    (x3, y3, _z3), (vx3, vy3, vz3) = stones[2]
    x, y, z = Reals("x y z")
    vx, vy, vz = Reals("dx dy dz")
    t1, t2, t3 = Reals("t1 t2 t3")
    solver = Solver()
    solver.add(
        x + t1 * vx == x1 + t1 * vx1,
        x + t2 * vx == x2 + t2 * vx2,
        x + t3 * vx == x3 + t3 * vx3,
        y + t1 * vy == y1 + t1 * vy1,
        y + t2 * vy == y2 + t2 * vy2,
        y + t3 * vy == y3 + t3 * vy3,
        z + t1 * vz == z1 + t1 * vz1,
        z + t2 * vz == z2 + t2 * vz2,
        z + t3 * vz == _z3 + t3 * vz3,
    )
    solver.check()
    model = solver.model()
    return model[x].as_long() + model[y].as_long() + model[z].as_long()


def run():
    stones = []
    for line in read_n_lines_one_string():
        positions, velocities = line.split(' @ ')
        stones.append((list_to_int(positions.split(', ')),
                       list_to_int(velocities.split(', '))))

    print(task1(stones))
    print(task2(stones))


if __name__ == "__main__":
    run()
