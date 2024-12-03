import re

if __name__ == "__main__":
    with open("day3.txt", "r") as f:
        corrupt_memory = f.read()

    search_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(search_pattern, corrupt_memory)
    print(f"Part 1: {sum([int(x) * int(y) for x, y in matches])}")

    search_pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    process_instructions = True
    instruction_sum = 0
    for match in re.finditer(search_pattern, corrupt_memory):
        if match[0] == "do()": 
            process_instructions = True
        elif match[0] == "don't()": 
            process_instructions = False
        elif process_instructions:
            instruction_sum += int(match[1]) * int(match[2])

    print(f"Part 2: {instruction_sum}")