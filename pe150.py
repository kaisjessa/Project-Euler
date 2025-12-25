from math import inf


def make_triangle(num_rows):
    arr = []
    t = 0
    for i in range(1, num_rows + 1):
        row = []
        for _ in range(i):
            t = (615949 * t + 797807) % 2**20
            row.append(t - 2**19)
        arr.append(row)
    return arr


def sub_triangle_sums(triangle):
    num_rows = len(triangle)
    min_sum = inf
    T0 = []
    T1 = []
    for i in range(num_rows):
        temp0 = []
        temp1 = []
        for j in range(len(triangle[i])):
            temp0.append(triangle[i][j])
            min_sum = min(min_sum, triangle[i][j])
            if i < num_rows - 1:
                t = triangle[i][j] + triangle[i + 1][j] + triangle[i + 1][j + 1]
                temp1.append(t)
                min_sum = min(min_sum, t)
        T0.append(temp0)
        if i < num_rows - 1:
            T1.append(temp1)
    for k in range(2, num_rows):
        Tk = []
        for i in range(num_rows - k):
            temp = []
            for j in range(len(triangle[i])):
                t = triangle[i][j] + T1[i + 1][j] + T1[i + 1][j + 1] - T0[i + 2][j + 1]
                temp.append(t)
                min_sum = min(min_sum, t)
            Tk.append(temp)
        T0 = T1
        T1 = Tk
    return min_sum


# def lowest_sum(triangle):
#     num_rows = len(triangle[-1])
#     min_sum = min(triangle[-1])
#     # sums = []
#     # for row in triangle:
#     #     arr = []
#     #     for e in row:
#     #         arr.append(e)
#     #     sums.append(arr)
#     for i in range(num_rows - 2, -1, -1):
#         print(i)
#         for j in range(0, i + 1):
#             totals = [triangle[i][j]]
#             index = 2
#             for k in range(i + 1, num_rows, 1):
#                 # print(i, j, k, index)
#                 row_sum = sum(triangle[k][l] for l in range(j, j + index))
#                 row_sum += totals[-1]
#                 totals.append(row_sum)
#                 index += 1
#             # print(i, j, totals)
#             min_sum = min(min_sum, min(totals))
#     return min_sum


if __name__ == "__main__":
    triangle = make_triangle(1000)
    # triangle = [
    #     [15],
    #     [-14, -7],
    #     [20, -13, -5],
    #     [-3, 8, 23, -26],
    #     [1, -4, -5, -18, 5],
    #     [-16, 31, 2, 9, 28, 3],
    # ]
    # print(len(triangle))
    # print(lowest_sum(triangle))
    sol = sub_triangle_sums(triangle)
    print(sol)
