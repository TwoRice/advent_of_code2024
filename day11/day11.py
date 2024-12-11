from collections import defaultdict

def blink(stones):
    for engraving, count in list(stones.items()):
        if count == 0:
            continue
        stones[engraving] -= count
        if engraving == 0:
            stones[1] += count
        elif len(str(engraving)) % 2 == 0:
            str_engraving = str(engraving)
            first_half = int(str_engraving[:len(str_engraving) // 2])
            second_half = int(str_engraving[len(str_engraving) // 2:])
            stones[first_half] += count
            stones[second_half] += count
        else:
            stones[engraving * 2024] += count

if __name__ == "__main__":
    with open("day11.txt", "r") as f:
        stones = [int(engraving) for engraving in f.read().split()]

    stone_engraving_counts = defaultdict(int, {engraving: 1 for engraving in stones})
    for _ in range(25):
        blink(stone_engraving_counts)
    print(f"Part 1: {sum([x for x in stone_engraving_counts.values()])}")

    for _ in range(50):
        blink(stone_engraving_counts)
    print(f"Part 2: {sum([x for x in stone_engraving_counts.values()])}") 