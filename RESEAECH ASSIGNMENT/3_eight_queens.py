# 8 Queens Problem - solved using Backtracking
N = 8

def is_safe(board, row, col):
    """board[r] = column of the queen in row r. Check column and diagonal clashes."""
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

def solve(board, row, solutions):
    if row == N:                       # all 8 queens placed
        solutions.append(board[:])
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, solutions)
            board[row] = -1            # backtrack

def print_board(board):
    for r in range(N):
        print(" ".join("Q" if board[r] == c else "." for c in range(N)))

if __name__ == "__main__":
    solutions = []
    solve([-1] * N, 0, solutions)
    print(f"Total solutions for {N}-Queens: {len(solutions)}\n")
    print("First solution:")
    print_board(solutions[0])
    print("\nQueen positions (row, column):", [(r + 1, c + 1) for r, c in enumerate(solutions[0])])
