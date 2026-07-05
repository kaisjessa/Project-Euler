import time
import copy
from random import randint
from functools import lru_cache


@lru_cache(maxsize=None)
def brute_force(s, n, m):
    # function input is board as a string
    # for caching
    board = str_to_list(s, n, m)
    # base case: if board is full, we have found a tiling
    if all(0 not in row for row in board):
        return 1
    count = 0
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            # top-left most empty cell
            if col == 0:
                # print(i, j)
                # X X X
                if j + 2 < len(row) and board[i][j + 1] == 0 and board[i][j + 2] == 0:
                    board[i][j] = 1
                    board[i][j + 1] = 1
                    board[i][j + 2] = 1
                    s = list_to_str(board)
                    count += brute_force(s, n, m)
                    board[i][j] = 0
                    board[i][j + 1] = 0
                    board[i][j + 2] = 0
                # X
                # X
                # X
                if i + 2 < len(board) and board[i + 1][j] == 0 and board[i + 2][j] == 0:
                    board[i][j] = 1
                    board[i + 1][j] = 1
                    board[i + 2][j] = 1
                    s = list_to_str(board)
                    count += brute_force(s, n, m)
                    board[i][j] = 0
                    board[i + 1][j] = 0
                    board[i + 2][j] = 0
                # X X
                #   X
                if (
                    j + 1 < len(row)
                    and i + 1 < len(board)
                    and board[i][j + 1] == 0
                    and board[i + 1][j + 1] == 0
                ):
                    board[i][j] = 1
                    board[i][j + 1] = 1
                    board[i + 1][j + 1] = 1
                    s = list_to_str(board)
                    count += brute_force(s, n, m)
                    board[i][j] = 0
                    board[i][j + 1] = 0
                    board[i + 1][j + 1] = 0

                # X X
                # X
                if (
                    j + 1 < len(row)
                    and i + 1 < len(board)
                    and board[i][j + 1] == 0
                    and board[i + 1][j] == 0
                ):
                    board[i][j] = 1
                    board[i][j + 1] = 1
                    board[i + 1][j] = 1
                    s = list_to_str(board)
                    count += brute_force(s, n, m)
                    board[i][j] = 0
                    board[i][j + 1] = 0
                    board[i + 1][j] = 0

                # X
                # X X
                if (
                    j + 1 < len(row)
                    and i + 1 < len(board)
                    and board[i + 1][j] == 0
                    and board[i + 1][j + 1] == 0
                ):
                    board[i][j] = 1
                    board[i + 1][j] = 1
                    board[i + 1][j + 1] = 1
                    s = list_to_str(board)
                    count += brute_force(s, n, m)
                    board[i][j] = 0
                    board[i + 1][j] = 0
                    board[i + 1][j + 1] = 0
                #   X
                # X X
                if (
                    j - 1 >= 0
                    and i + 1 < len(board)
                    and board[i + 1][j] == 0
                    and board[i + 1][j - 1] == 0
                ):
                    board[i][j] = 1
                    board[i + 1][j] = 1
                    board[i + 1][j - 1] = 1
                    s = list_to_str(board)
                    count += brute_force(s, n, m)
                    board[i][j] = 0
                    board[i + 1][j] = 0
                    board[i + 1][j - 1] = 0
                return count


def list_to_str(board):
    b = ["".join([str(s) for s in row]) for row in board]
    s = "".join(b)
    return s


def str_to_list(s, n, m):
    board = [[int(d) for d in s[i * n : i * n + n]] for i in range(m)]
    return board


def solve():
    n, m = 9, 12
    board = [[0 for i in range(n)] for i in range(m)]
    s = list_to_str(board)
    return brute_force(s, n, m)


if __name__ == "__main__":
    start = time.time()
    print(solve())
    print(f"Finished in {round(time.time()-start,2)}s")
