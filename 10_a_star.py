# A* Algorithm - shortest path on a grid  (f(n) = g(n) + h(n))
# g(n) = steps taken from the start, h(n) = Manhattan distance to the goal
# S = start, G = goal, # = wall, . = free cell
import heapq

GRID = [
    "S . . . . .",
    "# # . # # .",
    ". . . . # .",
    ". # # . . .",
    ". . . . # G",
]

def parse(grid):
    cells = [row.split() for row in grid]
    for r, row in enumerate(cells):
        for c, ch in enumerate(row):
            if ch == "S":
                start = (r, c)
            elif ch == "G":
                goal = (r, c)
    return cells, start, goal

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(cells, start, goal):
    rows, cols = len(cells), len(cells[0])
    open_list = [(heuristic(start, goal), 0, start)]      # (f, g, position)
    parent = {start: None}
    best_g = {start: 0}
    expanded = 0
    while open_list:
        f, g, current = heapq.heappop(open_list)          # node with the smallest f
        if g > best_g[current]:
            continue                                      # outdated entry
        expanded += 1
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], expanded
        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # up, down, left, right
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and cells[nr][nc] != "#":
                new_g = g + 1
                if new_g < best_g.get((nr, nc), float("inf")):
                    best_g[(nr, nc)] = new_g
                    parent[(nr, nc)] = current
                    heapq.heappush(open_list, (new_g + heuristic((nr, nc), goal), new_g, (nr, nc)))
    return None, expanded

if __name__ == "__main__":
    cells, start, goal = parse(GRID)
    print("Grid (S = start, G = goal, # = wall):")
    print("\n".join(GRID))
    path, expanded = a_star(cells, start, goal)
    if path is None:
        print("\nNo path exists.")
    else:
        for r, c in path[1:-1]:
            cells[r][c] = "*"
        print("\nPath found (* marks the path):")
        for row in cells:
            print(" ".join(row))
        print("\nPath (row, col):", path)
        print("Path cost (steps):", len(path) - 1)
        print("Nodes expanded   :", expanded)
