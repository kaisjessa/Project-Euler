import math 

matrix = []
with open("pe081_matrix.txt", "r") as f:
    for line in f.readlines():
        matrix.append([int(i) for i in line.strip().split(',')])

# matrix = [
#     [131, 673, 234, 103, 18],
#     [201, 96, 342, 965, 150],
#     [630, 803, 746, 422, 111],
#     [537, 699, 497, 121, 956],
#     [805, 732, 524, 37, 331]
#     ]

if __name__ == "__main__":
    n = len(matrix)
    paths = [[math.inf for i in range(n)] for i in range(n)]
    for i in range(n):
        paths[i][0] = matrix[i][0]
    for j in range(1, n):
        for i in range(n):
            paths[i][j] = paths[i][j-1] + matrix[i][j]
            for k in range(0, i, 1):
                paths[i][j] = min(paths[i][j], paths[k][j-1] + sum([matrix[l][j] for l in range(k, i+1)]))
            for k in range(i+1, n, 1):
                paths[i][j] = min(paths[i][j], paths[k][j-1] + sum([matrix[l][j] for l in range(i, k+1)]))
    print(min([paths[i][-1] for i in range(n)]))