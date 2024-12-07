import numpy as np

def simulate_guard_patrol(lab_map, position):
    turn_count = 0
    direction_vectors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = direction_vectors[turn_count]
    visited = {position}
    loop_check = {(position, direction)}
    while position[1] > 0 and position[1] < lab_map.shape[1] - 1 and position[0] > 0 and position[0] < lab_map.shape[0] - 1:
        next_position = position[0] + direction[0], position[1] + direction[1] 
        if lab_map[next_position] != "#":
            position = next_position
            if (position, direction) in loop_check:
                return False
            visited.add(position)
            loop_check.add((position, direction))
        else:
            turn_count = (turn_count + 1) % 4
            direction = direction_vectors[turn_count]

    return visited

if __name__ == "__main__":
    with open("day6.txt", "r") as f:
        lab_map = np.array([np.array(list(line)) for line in f.read().split("\n")])

        start_y, start_x = np.where(lab_map == "^")
        start_position = (start_y[0], start_x[0])

        visited = simulate_guard_patrol(lab_map, start_position)
        print(f"Part 1: {len(visited)}")

        possible_loop_count = 0
        obstruction_positions = visited - {start_position}
        for obsruction in obstruction_positions:
            new_lab_map = lab_map.copy()
            new_lab_map[obsruction] = "#"

            if not simulate_guard_patrol(new_lab_map, start_position):
                possible_loop_count += 1

        print(f"Part 2: {possible_loop_count}")