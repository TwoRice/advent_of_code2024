import numpy as np

with open("day4.txt") as f:
    word_search = np.array([np.array(list(line.strip())) for line in f.readlines()])

straight_count = 0
for _ in range(4):
    word_search = np.rot90(word_search)
    straight_count += sum([''.join(line).count("XMAS") for line in word_search])

diagonal_count = 0
for _ in range(4):
    word_search = np.rot90(word_search)
    diagonal_count += sum([''.join(np.diagonal(word_search, i)).count("XMAS") for i in range(len(word_search) - 3)])
    diagonal_count += sum([''.join(np.diagonal(word_search, i+1, axis1=1, axis2=0)).count("XMAS") for i in range(len(word_search) - 3)])

print(f"Part 1: {straight_count + diagonal_count}")

xmas_count = 0
for i in range(len(word_search) - 2):
    for j in range(len(word_search) - 2):
        window = word_search[i:i+3, j:j+3]
        for _ in range(4):
            window = np.rot90(window)
            diag1 = ''.join(np.diagonal(window))
            diag2 = ''.join(np.diagonal(np.rot90(window)))
    
            if diag1 == "MAS" and diag2 == "MAS":
                xmas_count += 1

print(f"Part 2: {xmas_count}")