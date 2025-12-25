from math import inf


def lagged_fibonacci_generator(square):
    arr = [0 for i in range(square**2 + 1)]
    for k in range(1, min(square**2 + 1, 55 + 1)):
        arr[k] = (100003 - 200003 * k + 300007 * k**3) % 1000000 - 500000
        # print(k, arr[k])
    for k in range(56, square**2 + 1):
        arr[k] = (arr[k - 24] + arr[k - 55] + 1000000) % 1000000 - 500000
        # print(k, k - 24, k - 55, arr[k])
    return arr


def best_row_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    sums = [[-inf for _ in range(m)] for _ in range(n)]
    for i in range(n):
        sums[i][0] = matrix[i][0]
        for j in range(1, m):
            sums[i][j] = max(matrix[i][j], sums[i][j - 1] + matrix[i][j])
    return max(max(a for a in row) for row in sums)


def best_col_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    sums = [[-inf for _ in range(m)] for _ in range(n)]
    for j in range(m):
        sums[0][j] = matrix[0][j]
        for i in range(1, n):
            sums[i][j] = max(matrix[i][j], sums[i - 1][j] + matrix[i][j])
    return max(max(a for a in row) for row in sums)


def best_diag_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    sums = [[-inf for _ in range(m)] for _ in range(n)]
    for i in range(n):
        sums[i][-1] = matrix[i][-1]
    for j in range(m):
        sums[0][j] = matrix[0][j]
    for i in range(1, n):
        for j in range(0, m - 1):
            sums[i][j] = max(matrix[i][j], sums[i - 1][j + 1] + matrix[i][j])
    return max(max(a for a in row) for row in sums)


def best_anti_diag_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    sums = [[-inf for _ in range(m)] for _ in range(n)]
    for i in range(n):
        sums[i][0] = matrix[i][0]
    for j in range(m):
        sums[0][j] = matrix[0][j]
    for i in range(1, n):
        for j in range(1, m):
            sums[i][j] = max(matrix[i][j], sums[i - 1][j - 1] + matrix[i][j])
    return max(max(a for a in row) for row in sums)


if __name__ == "__main__":
    sq = 2000
    arr = lagged_fibonacci_generator(sq)
    # print(len(arr))

    matrix = []
    for n in range(sq):
        matrix.append(arr[sq * n : sq * (n + 1)])

    # print(matrix)
    # matrix = [[-2, 5, 3, 2], [9, -6, 5, 1], [3, 2, 7, 3], [-1, 8, -4, 8]]
    a = best_row_sum(matrix)
    b = best_col_sum(matrix)
    c = best_diag_sum(matrix)
    d = best_anti_diag_sum(matrix)
    print(max(a, b, c, d))
