# Missionaries and Cannibals Problem - solved using Breadth First Search (BFS)
# State = (missionaries on left, cannibals on left, boat side: 'L' or 'R')
from collections import deque

TOTAL_M, TOTAL_C, BOAT = 3, 3, 2
MOVES = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]   # (missionaries, cannibals) in boat

def is_valid(m, c):
    """Missionaries must never be outnumbered by cannibals on either bank."""
    if not (0 <= m <= TOTAL_M and 0 <= c <= TOTAL_C):
        return False
    rm, rc = TOTAL_M - m, TOTAL_C - c
    if m > 0 and c > m:
        return False
    if rm > 0 and rc > rm:
        return False
    return True

def solve():
    start, goal = (TOTAL_M, TOTAL_C, "L"), (0, 0, "R")
    queue = deque([(start, [(start, "Start")])])
    visited = {start}
    while queue:
        (m, c, side), path = queue.popleft()
        if (m, c, side) == goal:
            return path
        for dm, dc in MOVES:
            if side == "L":
                nm, nc, nside = m - dm, c - dc, "R"
            else:
                nm, nc, nside = m + dm, c + dc, "L"
            state = (nm, nc, nside)
            if is_valid(nm, nc) and state not in visited:
                visited.add(state)
                direction = "->" if side == "L" else "<-"
                action = f"Move {dm}M {dc}C {direction}"
                queue.append((state, path + [(state, action)]))
    return None

if __name__ == "__main__":
    path = solve()
    print(f"{'Step':<5}{'Action':<18}{'Left bank (M,C)':<18}{'Right bank (M,C)':<18}Boat")
    for i, ((m, c, side), action) in enumerate(path):
        left = f"({m},{c})"
        right = f"({TOTAL_M - m},{TOTAL_C - c})"
        print(f"{i:<5}{action:<18}{left:<18}{right:<18}{'Left' if side == 'L' else 'Right'}")
    print(f"\nAll people crossed in {len(path) - 1} crossings.")
