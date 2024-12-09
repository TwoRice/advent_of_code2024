def expand_disk_map(disk_map, one_dim=True):
    expanded_disk_map = []
    for file_id, i in enumerate(range(0, len(disk_map), 2)):
        file_size = int(disk_map[i])
        if one_dim:
            expanded_disk_map.extend([str(file_id)] * file_size)
        else:
            expanded_disk_map.append([str(file_id)] * file_size)
        if i < len(disk_map) - 1:
            free_space = int(disk_map[i+1])
            if one_dim:
                expanded_disk_map.extend(["."] * free_space)
            elif free_space > 0:
                expanded_disk_map.append(["."] * free_space)

    return expanded_disk_map

def calc_checksum(expanded_disk_map):
    checksum = 0
    for i, file_block in enumerate(expanded_disk_map):
        if file_block == ".": continue
        checksum += i * int(file_block)
    
    return checksum

if __name__ == "__main__":
    with open("day9.txt", "r") as f:
        disk_map = f.read()

    expanded_disk_map = expand_disk_map(disk_map)
    free_space = [idx for idx, value in enumerate(expanded_disk_map) if value == "."]
    file_blocks = [idx for idx, value in enumerate(expanded_disk_map) if value != "."]
    for i, file_block in enumerate(file_blocks[::-1]):
        if file_block <= free_space[i]: break
        expanded_disk_map[free_space[i]] = str(expanded_disk_map[file_block])
        expanded_disk_map[file_block] = "."

    print(f"Part 1: {calc_checksum(expanded_disk_map)}")

    expanded_disk_map = expand_disk_map(disk_map, one_dim=False)
    free_space = {idx: len(value) for idx, value in enumerate(expanded_disk_map) if value[0] == "."}
    file_blocks = [(idx, len(value)) for idx, value in enumerate(expanded_disk_map) if value[0] != "."]
    for i, (file_block, file_size) in enumerate(file_blocks[::-1]):
        for idx, space in free_space.items():
            if idx >= file_block: break

            if file_size <= space:
                remaining_space = space - file_size
                start_idx = expanded_disk_map[idx].index(".")
                expanded_disk_map[idx] = expanded_disk_map[idx][:start_idx] + expanded_disk_map[file_block] + ["."] * remaining_space
                free_space[idx] = remaining_space
                expanded_disk_map[file_block] = ["."] * file_size
                break

    print(f"Part 2: {calc_checksum([inner for outer in expanded_disk_map for inner in outer])}")