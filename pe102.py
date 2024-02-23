
def get_triangles():
    coords = []
    with open("files/pe102_triangles.txt", 'r') as f:
        for l in f.readlines():
            c = l.split(',')
            a = (int(c[0]), int(c[1]))
            b = (int(c[2]), int(c[3]))
            c = (int(c[4]), int(c[5]))
            coords.append([a,b,c])
    return coords

def above_origin(p1, p2):
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    b = p2[1]-(m*p2[0])
    return b >= 0 and min(p1[1], p2[1]) <= b and b <= max(p1[1], p2[1])

def below_origin(p1, p2):
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    b = p2[1]-(m*p2[0])
    return b <= 0 and min(p1[1], p2[1]) <= b and b <= max(p1[1], p2[1])

if __name__ == "__main__":
    coords = get_triangles()
    total = 0
    for cd in coords:
        a,b,c = cd
        if(not (a[0] < 0 and b[0] < 0 and c[0] < 0 or a[0] > 0 and b[0] > 0 and c[0] > 0 or a[1] < 0 and b[1] < 0 and c[1] < 0 or a[1] > 0 and b[1] > 0 and c[1] > 0)):
            if(above_origin(a,b) or above_origin(b,c) or above_origin(a,c)):
                if(below_origin(a,b) or below_origin(b,c) or below_origin(a,c)):
                    total += 1
                    # print(a,b,c)
    print(total)
