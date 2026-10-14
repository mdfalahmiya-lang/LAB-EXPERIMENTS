# 8 Puzzle Problem - solved using A* Search (Manhattan distance heuristic)
import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)          # 0 represents the blank tile
START = (1, 2, 3,
         5, 6, 0,
         7, 8, 4)         # change this to try other puzzles

def manhattan(state):
    """Sum of distances of each tile from its goal position."""
    total = 0
    for i, tile in enumerate(state):
        if tile != 0:
            g = GOAL.index(tile)
            total += abs(i // 3 - g // 3) + abs(i % 3 - g % 3)
    return total

def is_solvable(state):
    """A 3x3 puzzle is solvable only if the number of inversions is even."""
    tiles = [t for t in state if t != 0]
    inv = sum(1 for i in range(len(tiles)) for j in range(i + 1, len(tiles))
              if tiles[i] > tiles[j])
    return inv % 2 == 0

def neighbors(state):
    """Generate all states reachable by sliding one tile into the blank."""
    b = state.index(0)
    r, c = divmod(b, 3)
    for dr, dc, move in [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            n = nr * 3 + nc
            s = list(state)
            s[b], s[n] = s[n], s[b]
            yield tuple(s), move

def solve(start):
    pq = [(manhattan(start), 0, start, [])]   # (f, g, state, path)
    visited = set()
    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == GOAL:
            return path
        if state in visited:
            continue
        visited.add(state)
        for nxt, move in neighbors(state):
            if nxt not in visited:
                heapq.heappush(pq, (g + 1 + manhattan(nxt), g + 1, nxt, path + [(move, nxt)]))
    return None

def show(state):
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x else "_" for x in state[i:i + 3]))
    print()

if __name__ == "__main__":
    if not is_solvable(START):
        print("This puzzle cannot be solved.")
    else:
        print("Start State:")
        show(START)
        solution = solve(START)
        for step, (move, state) in enumerate(solution, 1):
            print(f"Step {step}: Move blank {move}")
            show(state)
        print(f"Goal reached in {len(solution)} moves.")
