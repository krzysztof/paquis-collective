from collections import deque
import sys
import os

class PrecomputedPizza:
    def __init__(self, pizza):
        self.pizza = pizza
        self.precompute()

    def precompute(self):
        pizza = self.pizza
        nrows = len(pizza)
        ncols = len(pizza[0])
        # [T, M]
        dp = [[[0,0] for _ in range(ncols + 1)] for _ in range(nrows + 1)]
        # i,j shifted by 1
        for r in range(1, nrows+1):
            for c in range(1, ncols+1):
                dp[r][c][0] = dp[r-1][c][0] + dp[r][c-1][0] - dp[r-1][c-1][0] + (1 if pizza[r-1][c-1] == 'T' else 0)
                dp[r][c][1] = dp[r-1][c][1] + dp[r][c-1][1] - dp[r-1][c-1][1] + (1 if pizza[r-1][c-1] == 'M' else 0)
        self.dp = dp

    def ingrid(self, i, j, k, l):
        ingridients = []
        for ingr in [0, 1]:
            cnt = self.dp[k + 1][l + 1][ingr] + self.dp[i][j][ingr] -\
                self.dp[k + 1][j][ingr] - self.dp[i][l+1][ingr]
            ingridients.append(cnt)
        return min(ingridients)

infile = sys.argv[1]
with open(infile, 'r') as fp:
    lines = [l.strip() for l in fp.readlines()]

nrow, ncol, L, M = list(map(int, lines[0].split(' ')))

pizza = lines[1:]
pizzaDP = PrecomputedPizza(pizza)
print(pizzaDP.ingrid(0, 0, 0, 0))

def getArea(r,c,r2,c2):
    return (r2 - r + 1) * (c2 - c + 1)

def compScore(sl):
    Li = pizzaDP.ingrid(*sl)
    A = getArea(*sl)
    if Li >= L and A <= M:
        return A, True
    else:
        return 0, False

from copy import deepcopy as dpc
maxsplitsA = -1
maxsplits = None
solidx = 0


def write_sol():
    global solidx
    def get_solution_string(splits):
        out = str(len(splits)) + '\n'
        for sp in splits:
            sp, cnt = sp
            out += " ".join(map(str, sp)) + '\n'
        return out
    sol = get_solution_string(maxsplits)

    outfile = infile+'.out'+ '.{}'.format(str(solidx).zfill(6)) + "_" + str(maxsplitsA)
    solidx += 1

    with open("outs/" + outfile, 'w') as fp:
        fp.write(sol)


def find():
    global maxsplitsA
    global maxsplits

    q = deque()
    q.append(([0, 0, nrow - 1, ncol - 1], []))
    while q:
        sp, cursplits = q.pop()

        r, c, r2, c2 = sp
        A = getArea(r, c, r2, c2)
        if A < (2 * L):
            continue

        S0, valid = compScore(sp)
        S0new = (sum(s for _, s in cursplits) + S0)
        if  S0new > maxsplitsA and valid:
            maxsplitsA = S0new
            maxsplits = dpc(cursplits) + [(sp,S0)]
            write_sol()

        for colsp in range(c2 - c - 1):  # 0-> n-1 splits

            spA = [r, c, r2, c + colsp]
            S, valid = compScore(spA)

            spB = [r, c + colsp + 1, r2, c2]
            S2, valid2 = compScore(spB)

            cursplits2 = dpc(cursplits) + ([(spA, S), ] if valid else [])
            q.append([spB, cursplits2])
            cursplits2 = dpc(cursplits) + ([(spB, S2), ] if valid2 else [])
            q.append([spA, cursplits2])
        for rowsp in range(r2 - r - 1):
            spA = [r, c, r + rowsp, c2]
            S, valid = compScore(spA)

            spB = [r + rowsp + 1, c, r2, c2]
            S2, valid2 = compScore(spB)

            cursplits2 = dpc(cursplits) + ([(spA, S), ] if valid else [])
            q.append([spB, cursplits2])
            cursplits2 = dpc(cursplits) + ([(spB, S2), ] if valid2 else [])
            q.append([spA, cursplits2])

find()
