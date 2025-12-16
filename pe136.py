if __name__ == "__main__":
    goal = 50_000_000
    sols = [0]*goal
    for z in range(1, goal+1, 1):
        for k in range(z//3, goal, 1):
            n = (k+z)*(3*k-z)
            # k increases => n increases
            if(n >= goal):
                break
            if(n <= 0):
                continue
            sols[n] += 1
    print(len([n for n in range(goal) if sols[n]==1]))