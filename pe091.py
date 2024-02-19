import math

def is_right_triangle(c1, c2, c3):
    s1 = (c2[0]-c1[0])**2 + (c2[1]-c1[1])**2
    s2 = (c3[0]-c2[0])**2 + (c3[1]-c2[1])**2
    s3 = (c3[0]-c1[0])**2 + (c3[1]-c1[1])**2
    ls = sorted([s1, s2, s3])
    return ls[0] + ls[1] == ls[2]

def compute_triangles(n: int):
    c1 = (0,0)
    all_coords = [(i,j) for i in range(n+1) for j in range(n+1)][1:]
    l = len(all_coords)
    count = 0
    for i in range(l-1):
        c2 = all_coords[i]
        for j in range(i+1, l):
            c3 = all_coords[j]
            # determine if (c1, c2, c3) forms a right triangle
            if(is_right_triangle(c1, c2, c3)):
                count += 1
                #print(c1, c2, c3)
    return count

if __name__ == "__main__":
    n = 50
    print(compute_triangles(n))