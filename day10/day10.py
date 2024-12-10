import numpy as np

def dfs(graph, node_coords, visited):
    visited.append(tuple(node_coords))
    node = graph[*node_coords]

    search_directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for direction in search_directions:
        next_coords = node_coords + direction
        if next_coords[0] >= 0 and next_coords[0] < graph.shape[0] and next_coords[1] >= 0 and next_coords[1] < graph.shape[1]:
            next_node = graph[*next_coords]
            if tuple(next_coords) not in visited and next_node == node + 1:
                dfs(graph, next_coords, visited.copy())
    visited_list.append(visited)

if __name__ == "__main__":
    with open("day10.txt", "r") as f:
        topo_map = np.array([np.array(list(row)) for row in f.read().split("\n")], dtype=int)

    trailheads = np.argwhere(topo_map == 0)

    total_trails = 0
    total_rating = 0
    for trailhead in trailheads:
        visited_list = []
        dfs(topo_map, trailhead, [])
        unique_nodes = {node for trail in visited_list for node in trail}
        total_trails += sum([topo_map[node] == 9 for node in unique_nodes])
        total_rating += sum([topo_map[node] == 9 for trail in visited_list for node in trail])

    print(f"Part 1: {total_trails}")
    print(f"Part 2: {total_rating}")