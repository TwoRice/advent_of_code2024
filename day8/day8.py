import numpy as np
from itertools import combinations

def check_in_bounds(vector, map_shape):
    return vector[0] >= 0 and vector[0] < map_shape[0] and vector[1] >= 0 and vector[1] < map_shape[1]

def calculate_antinodes(starting_pos, difference_vector):
    antinode_set = set()
    antinode = tuple(starting_pos)
    while(True):
        antinode_set.add(antinode)
        antinode = tuple(antinode + difference_vector)
        if not check_in_bounds(antinode, antenna_map.shape):
            return antinode_set

if __name__ == "__main__":
    with open("day8.txt", "r") as f:
        antenna_map = np.array([np.array(list(row)) for row in f.read().split("\n")])

    antenna_freqs = np.unique(antenna_map) 
    antenna_freqs = np.delete(antenna_freqs, np.where(antenna_freqs == "."))

    unique_antinodes = set()
    for freq in antenna_freqs:
        antenna_locs = np.argwhere(antenna_map == freq)
        antenna_pairs = combinations(antenna_locs, 2)
        for pair in antenna_pairs:
            difference_vector = pair[0] - pair[1]
            antinode1 = tuple(pair[0] + difference_vector)
            antinode2 = tuple(pair[1] - difference_vector)
            if check_in_bounds(antinode1, antenna_map.shape):
                unique_antinodes.add(antinode1)
            if check_in_bounds(antinode2, antenna_map.shape):
                unique_antinodes.add(antinode2)

    print("Part 1:", len(unique_antinodes))

    unique_antinodes = set()
    for freq in antenna_freqs:
        antenna_locs = np.argwhere(antenna_map == freq)
        antenna_pairs = combinations(antenna_locs, 2)
        for pair in antenna_pairs:
            difference_vector = pair[0] - pair[1]
            unique_antinodes = unique_antinodes.union(calculate_antinodes(pair[0], difference_vector))
            unique_antinodes = unique_antinodes.union(calculate_antinodes(pair[1], -1 * difference_vector))

    print("Part 2:", len(unique_antinodes))