import math

# for x*y*z cuboid, gives the number of cubes in layer l
def f(x,y,z,l):
    if(l == 1):
        return 2*(x*y + y*z + x*z)
    else:
        return (f(x,y,z,l-1) + 4*(x+y+z) + 8*(l-2))
    
def f2(x,y,z,l):
    return 2*(x*y + y*z + x*z) + 4*(l-1)*(x+y+z) + 8*(l-2)*(l-1)//2

def C(cube_limit):
    results = [0]*cube_limit
    for x in range(1, cube_limit):
        if(f2(x,1,1,1) > cube_limit):
                break
        for y in range(1, x+1):
            if(f2(x,y,1,1) > cube_limit):
                break
            for z in range(1, y+1):
                l = 1
                total = f2(x,y,z,l)
                while(total < cube_limit):
                    results[total] += 1
                    l += 1
                    total = f2(x,y,z,l)
    return results

if __name__ == "__main__":
    goal = 1000
    results = C(20000)
    if(goal in results):
        print(results.index(goal))