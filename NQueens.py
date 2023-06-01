def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True
def solve_n_queens_util(board, row, N):
    if row == N:
        return True
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens_util(board, row + 1, N):
                return True
    return False
def solve_n_queens(N):
    board = [-1] * N
    if solve_n_queens_util(board, 0, N):
        print("Solution Found:")
        for row in range(N):
            print(" ".join("1" if board[row] == col else "0" for col in range(N)))
        else:
            print("No solution found:")
N=4
solve_n_queens(N)