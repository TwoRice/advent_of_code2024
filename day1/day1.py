import numpy as np

if __name__ == "__main__":
    with open("day1.txt", "r") as f:
        location_lists = np.array([line.strip().split() for line in f.readlines()], dtype=int)

    print(f"Part 1: {sum(abs(np.sort(location_lists[:, 0]) - np.sort(location_lists[:, 1])))}")
    list_2_id_counts = dict(zip(*np.unique(location_lists[:, 1], return_counts=True)))
    print(f"Part 2: {sum([loc_id * list_2_id_counts[loc_id] for loc_id in location_lists[:, 0] if loc_id in list_2_id_counts])}")