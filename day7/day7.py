from itertools import product

def check_equation_validity(result, operands, valid_operators):
        operator_combos = product(valid_operators, repeat=len(operands)-1)
        for combo in operator_combos:
            equation_total = operands[0]
            for operator, operand in zip(combo, operands[1:]):
                if operator == "+":
                    equation_total += operand
                elif operator == "*":
                    equation_total *= operand
                else:
                    equation_total = int(str(equation_total) + str(operand))
            
            if equation_total == result:
                return result
            
        return 0

if __name__ == "__main__":
    with open("day7.txt", "r") as f:
        equations = [line.split(":") for line in f.read().split("\n")]

    part1 = part2 = 0
    for result, operands in equations:
        result = int(result)
        operands = [int(op) for op in operands.split()]
        part1 += check_equation_validity(result, operands, "+*")
        part2 += check_equation_validity(result, operands, "+*/")

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")