import math

matrix = []
with open("pe083_matrix.txt", "r") as f:
    for line in f.readlines():
        matrix.append([int(i) for i in line.strip().split(',')])

# matrix = [
#     [131, 673, 234, 103, 18],
#     [201, 96, 342, 965, 150],
#     [630, 803, 746, 422, 111],
#     [537, 699, 497, 121, 956],
#     [805, 732, 524, 37, 331]
#     ]

# given 0 <= i < n, 0 <= j < n
# return set of all coordinates that are neighbours of (i,j)
def get_neighbours(i, j, n):
    neighs = []
    if(i > 0):
        neighs.append((i-1, j))
    if(j > 0):
        neighs.append((i, j-1))
    if(i < n-1):
        neighs.append((i+1, j))
    if(j < n-1):
        neighs.append((i, j+1))
    return(neighs)

if __name__ == "__main__":
    n = len(matrix)
    # dijkstra's algorithm
    dists = [[math.inf for i in range(n)] for j in range(n)]
    visited = [[False for i in range(n)] for j in range(n)]
    dists[0][0] = matrix[0][0]
    x0, y0 = 0, 0
    while(not visited[n-1][n-1]):
        #print(x0, y0)
        nn = get_neighbours(x0, y0, n)
        for (x1,y1) in nn:
            if(not visited[x1][y1]):
                dists[x1][y1] = min(dists[x1][y1], dists[x0][y0] + matrix[x1][y1])
        visited[x0][y0] = True
        x0 = n-1
        y0 = n-1
        for tx in range(n):
            for ty in range(n):
                if(not visited[tx][ty] and dists[tx][ty] < dists[x0][y0]):
                    x0 = tx
                    y0 = ty
    print(dists[n-1][n-1])
        