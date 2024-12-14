import re
import math
import numpy as np

def check_solution(a, b):
    if math.isclose(a, round(a), rel_tol=0, abs_tol=1e-4) and math.isclose(b, round(b), rel_tol=0, abs_tol=1e-4):
        return 3*a + b
    return 0

if __name__ == "__main__":
    with open("day13.txt", "r") as f:
        machine_configs = [machine.split("\n") for machine in f.read().split("\n\n")]
    machine_configs = [
        [
            (int(re.search(r"X.(\d+)", m).group(1)), int(re.search(r"Y.(\d+)", m).group(1)))
            for m in machine
        ]
        for machine in machine_configs
    ]

    part1 = 0
    part2 = 0
    for button_a, button_b, prize in machine_configs:
        equations = [[button_a[0], button_b[0]], [button_a[1], button_b[1]]]
        a, b = np.linalg.solve(equations, [prize[0], prize[1]])
        part1 += check_solution(a, b)

        a, b = np.linalg.solve(equations, [prize[0] + 10000000000000, prize[1] + 10000000000000])
        part2 += check_solution(a, b)

    print(f"Part 1: {int(part1)}")
    print(f"Part 1: {int(part2)}")