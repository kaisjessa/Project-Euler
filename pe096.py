import sys
import os

grid = """080000040
000469000
400000007
005904600
070608030
008502100
900000005
000781000
060000010"""



class Square():
    def __init__(self, n: str):
        self.value = int(n)
        self.candidates = []

    def __repr__(self):
        return f"{self.value}, {self.candidates}"

class Puzzle():
    def __init__(self, sgrid: str):
        self.sgrid = sgrid
        self.grid = [[Square(x) for x in list(a)] for a in sgrid.split('\n')]
        self.valid = self.__update__()

    def __update__(self):
        for i in range(9):
            for j in range(9):
                current_square = self.grid[i][j]
                if(current_square.value == 0):
                    candidates = list(range(1,10))
                    for k in range(9):
                        if(self.grid[i][k].value in candidates):
                            candidates.remove(self.grid[i][k].value)
                        if(self.grid[k][j].value in candidates):
                            candidates.remove(self.grid[k][j].value)
                    si = 3*(i//3)
                    sj = 3*(j//3)
                    for k in range(si, si+3, 1):
                        for l in range(sj, sj+3, 1):
                            if((k,l) != (si, sj) and self.grid[k][l].value in candidates):
                                candidates.remove(self.grid[k][l].value)
                    if(len(candidates) == 0):
                        return False
                    current_square.candidates = candidates
        return True

    def __repr__(self):
        s = ""
        for i in range(9):
            for j in range(9):
                s += str(self.grid[i][j].value)
            s += "\n"
        return s
    
    def is_solved(self):
        if('0' in self.sgrid):
            return False
        # check each row and col
        for i in range(9):
            row = [v.value for v in self.grid[i]]
            if(sorted(row) != list(range(1,10))):
                return False
            col = [v.value for v in [self.grid[j][i] for j in range(9)]]
            if(sorted(col) != list(range(1,10))):
                return False
        # check each 3x3 square
        for si in range(0, 9, 3):
            for sj in range(0, 9, 3):
                l = []
                for i in range(si, si+3, 1):
                    for j in range(sj, sj+3, 1):
                        l.append(self.grid[i][j].value)
                if(sorted(l) != list(range(1,10))):
                    return False
        return True

    
    def get_neighbours(self):
        neighs = []
        for i in range(9):
            for j in range(9):
                current_square = self.grid[i][j]
                if(current_square.value == 0):
                    for c in current_square.candidates:
                        s = self.sgrid[:9*i+(j+i)] + str(c) + self.sgrid[9*i+(j+i+1):]
                        p = Puzzle(s)
                        if(p.valid and p not in neighs):
                            neighs.append(p)
                    return neighs
        return neighs
    
    def DFS(self):
        stack = [self]
        current = None
        while(len(stack) > 0):
            current = stack.pop(0)
            if(current.is_solved()):
                return current
            for v in current.get_neighbours():
                stack.append(v)
        return(current)


if __name__ == "__main__":
    with open("files/pe096_sudoku.txt", 'r') as f:
        grids = []
        i = 0
        c = ""
        for l in f.readlines():
            if(i % 10 == 0):
                grids.append(c[:-1])
                c = ""
            else:
                c += l
            i += 1
    total = 0
    for i in range(1, len(grids)):
        print(f"Solving Grid #{i}")
        p = Puzzle(grids[i])
        sol = p.DFS()
        print(sol.sgrid)
        total += int(sol.sgrid[:3])
    print(total)