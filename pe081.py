
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
    paths = [[0 for i in range(n)] for i in range(n)]
    paths[0][0] = matrix[0][0]
    for i in range(1, n):
        paths[0][i] = paths[0][i-1] + matrix[0][i]
        paths[i][0] = paths[i-1][0] + matrix[i][0]
    for i in range(1, n):
        for j in range(1, n):
            paths[i][j] = min(paths[i-1][j], paths[i][j-1]) + matrix[i][j]
    print(paths[-1][-1])