""" 
Write a program which return all distinct non-attacking placements of n queens on an n x n chessboard,
where n is an input to the program.
"""
import copy
import numpy as np

def take_input():
    """Accepts the size of the chess board"""
    size = int(input("Input size of the board: "))
    return size


def get_board(n):
    """Returns an n by n board"""
    board = np.zeros((n, n))
    return board


def print_solutions(sol, n):
    """Prints all solutions"""
    for s in sol:
        for r in s:
            print(r)
        print()


def is_safe(board, r, c, n):
    """Check if it's safe to place a queen at board[r][c]"""
    for y in range(c):
        if board[r][y] == 1:
            return False

    x, y = r, c
    while x >= 0 and y >= 0:
        if board[x][y] == 1:
            return False
        x, y = x - 1, y - 1

    x, y = r, c
    while x < n and y >= 0:
        if board[x][y] == 1:
            return False
        x, y = x + 1, y - 1

    return True


def solve(board, c, n):
    """Use backtracking to find all solutions"""
    if c >= n:
        return

    for i in range(n):
        if is_safe(board, i, c, n):
            board[i][c] = 1
            if c == n - 1:
                add_solution(board)
                board[i][c] = 0
            solve(board, c + 1, n)
            board[i][c] = 0


def add_solution(board):
    """Saves the board state to the global variable 'solutions'"""
    global solutions
    solutions.append(copy.deepcopy(board))


n = take_input()
board = get_board(n)
solutions = []
solve(board, 0, n)
print_solutions(solutions, n)

