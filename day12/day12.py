import numpy as np
from itertools import product

def bfs(graph, start):
    queue = [start]
    visited = set()
    perimeter = set()
    visited.add(start)

    search_directions = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
    while queue:
        node = queue.pop(0)
        for direction in search_directions:
            next_node = tuple(node + direction)
            if (
                next_node[0] >= 0 and next_node[0] < graph.shape[0] and
                next_node[1] >= 0 and next_node[1] < graph.shape[1] and
                graph[*next_node] == graph[*start]
            ):
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)
            else:
                perimeter.add((node, next_node))

    return visited, perimeter

if __name__ == "__main__":
    with open("day12.txt", "r") as f:
        garden_plots = np.array([np.array(list(row)) for row in f.read().split("\n")])

    total_cost = 0
    remaining_coords = set(product(range(garden_plots.shape[0]), range(garden_plots.shape[1])))
    plots = []
    while remaining_coords:
        plot_area, perimeter = bfs(garden_plots, remaining_coords.pop())
        plots.append(plot_area)
        total_cost += len(plot_area) * len(perimeter)
        remaining_coords -= plot_area
    print(f"Part 1: {total_cost}")

    total_cost = 0
    for plot in plots:
        corners = 0
        for y, x in plot:
            corners += (y + 1, x) not in plot and (y, x + 1) not in plot
            corners += (y - 1, x) not in plot and (y, x + 1) not in plot
            corners += (y + 1, x) not in plot and (y, x - 1) not in plot
            corners += (y - 1, x) not in plot and (y, x - 1) not in plot
            corners += (y + 1, x) in plot and (y, x + 1) in plot and (y + 1, x + 1) not in plot
            corners += (y - 1, x) in plot and (y, x + 1) in plot and (y - 1, x + 1) not in plot
            corners += (y + 1, x) in plot and (y, x - 1) in plot and (y + 1, x - 1) not in plot
            corners += (y - 1, x) in plot and (y, x - 1) in plot and (y - 1, x - 1) not in plot

        total_cost += len(plot) * corners
    print(f"Part 2: {total_cost}")