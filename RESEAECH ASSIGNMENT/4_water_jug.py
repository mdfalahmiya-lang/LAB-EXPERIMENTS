# Water Jug Problem - solved using Breadth First Search (BFS)
from collections import deque

def water_jug(cap_x, cap_y, target):
    start = (0, 0)                       # (water in jug X, water in jug Y)
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (x, y), path = queue.popleft()
        if x == target or y == target:
            return path
        pour_xy = min(x, cap_y - y)      # amount that can move X -> Y
        pour_yx = min(y, cap_x - x)      # amount that can move Y -> X
        next_states = [
            (cap_x, y),                  # fill X
            (x, cap_y),                  # fill Y
            (0, y),                      # empty X
            (x, 0),                      # empty Y
            (x - pour_xy, y + pour_xy),  # pour X into Y
            (x + pour_yx, y - pour_yx),  # pour Y into X
        ]
        for s in next_states:
            if s not in visited:
                visited.add(s)
                queue.append((s, path + [s]))
    return None

if __name__ == "__main__":
    cap_x = int(input("Enter capacity of jug X: "))
    cap_y = int(input("Enter capacity of jug Y: "))
    target = int(input("Enter target amount of water: "))
    path = water_jug(cap_x, cap_y, target)
    if path is None:
        print("No solution exists.")
    else:
        print("\nSteps (X, Y):")
        for i, state in enumerate(path):
            print(f"Step {i}: {state}")
        print(f"\nTarget reached in {len(path) - 1} steps.")
