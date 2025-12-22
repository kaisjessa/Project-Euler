def get_num_diag(n, m):
    # for each row in the grid
    # find the widest rectangle of each height
    # use that to find all rectangles of the same height starting at that row
    # lxh rectangle in row i -> l(l+1)//2 total rectangles of height h in row i
    # l hx1 + l-1 hx2 +  ... + 1 hxl
    grid = build_grid(n, m)
    d = len(grid)
    total = 0
    for h in range(1, d + 1):  # height
        for i in range(d - h + 1):  # row
            j = 0
            # first j in row where grid[i][j] and grid[i+h-1][j] = 1
            # meaning there is a hx1 rectangle starting at grid[i][j]
            while j < d and (grid[i][j] == 0 or grid[i + h - 1][j] == 0):
                j += 1
            if j >= d:
                continue
            first_index = j

            j = d - 1
            # last j in row where grid[i][j] and grid[i+h-1][j] == 1
            # meaning there is a h x (fi - j) rectangle with corners
            # grid[i][fi] x grid[i][j] x grid[i+h-1][j] x grid[i+h-1][fi]
            while j >= first_index and (grid[i][j] == 0 or grid[i + h - 1][j] == 0):
                j -= 1
            if j < first_index:
                continue
            last_index = j
            l = last_index - first_index + 1
            total += l * (l + 1) // 2
            # print(f"row: {i}, height: {h}, length: {l}, total_row: {l*(l+1)//2}")
    return total


# construct the diagonalized grid of squares
# 0: no square, 1: square
def build_grid(n, m):
    if m > n:
        n, m = m, n
    d = m + n - 2
    grid = [[0 for _ in range(d)] for _ in range(d)]
    si, sj = 0, d - n + 1
    down = 1
    for _ in range(2 * (m - 1) + 1):
        i = si
        j = sj
        for _ in range(n - down % 2):
            grid[i][j] = 1
            i += 1
            j += 1
        if down % 2 == 0:
            si += 1
        else:
            sj -= 1
        down += 1
    return grid


def get_num_straight(n, m):
    return n * (n + 1) // 2 * m * (m + 1) // 2


# def get_rows(n, m):
#     if m > n:
#         n, m = m, n
#     pows2 = [2 * k for k in range(1, m)]
#     lengths = pows2 + [2 * m - 1 for _ in range(n - m)] + pows2[::-1]
#     return lengths


if __name__ == "__main__":
    total = 0
    for n in range(1, 47 + 1):
        for m in range(1, 43 + 1):
            total += get_num_diag(n, m) + get_num_straight(n, m)
    print(total)
