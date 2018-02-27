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

    def area(self, i, j, k, l):
        ingridients = []
        for ingr in [0, 1]:
            cnt = self.dp[k + 1][l + 1][ingr] + self.dp[i][j][ingr] -\
                self.dp[k + 1][j][ingr] - self.dp[i][l+1][ingr]
            ingridients.append(cnt)
        return min(ingridients)

# pizza = [
#     'TTTTT',
#     'TMMMT',
#     'TTTTT'
# ]
# comp = PrecomputedPizza(pizza)
# print(comp.area(0, 0, 0, 0))

# Example:
#   area(0,0,1,1)
#
#    [TT]TTT,
#    [TM]MMT,
#     TT TTT

# def find(r, c, r2, c2):
#     L = 1
#     if comp.area(r, c, r2, c2) <= L:
#         for colsp in range(c+1, c2-1):
#             find(r, colsp, r2, colsp)
#         for rowsp in range(r+1, r2-1):
#             find(rowsp, c, rowsp, c2)

# find(0, 0, 3, 5)
