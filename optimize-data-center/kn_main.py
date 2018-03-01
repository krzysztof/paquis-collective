import random
import sys
import os

infile = sys.argv[1]
with open(infile, 'r') as fp:
    lines = [l.strip() for l in fp.readlines()]
# Usually first line specifies some numbers A, B, C, D, etc.:
R, S, U, P, M = [int(x) for x in lines[0].split(' ')]
# row, col
UU = list(map(lambda x: tuple(map(int, x.split(' '))), lines[1: U + 1]))
MM = list(map(lambda x: tuple(map(int, x.split(' '))), lines[U + 1:]))
#UU = [(l.split(' ')[0], l.split(' ')[1]) for l in lines[1: U + 1]]
# size, capacity
#MM = [(int(l.split(' ')[0]), int(l.split(' ')[1])) for l in lines[U + 1: ]]

MM = sorted(MM, key=lambda x: (x[1] / x[0], -x[0]))
MMchosen = [False, ] * len(MM)
import ipdb; ipdb.set_trace()

UNAV = -2
EMPTY = -1
grid = [[-1 for _ in range(S)] for _ in range(R)]
for ur, uc in UU:
    grid[ur][uc] = UNAV

inserted = True
colidx = [0,] * R
while inserted:
    inserted = False
    for row in range(R):
        col = colidx[row]
        while col < S and grid[row][col] == UNAV:
            col += 1





def write_output(data, prefix="", rnd=0):
    outfile = os.path.join('output', prefix, os.path.basename(infile) + '.output')
    if not os.path.exists(os.path.dirname(outfile)):
        os.mkdir(os.path.dirname(outfile))
    if rnd:
        outfile += ".{}".format(random.randint(10**rnd, 10**(rnd+1)))

    #
    # Modify how you write 'data'
    #
    with open(outfile, 'w') as fp:
        fp.write(data)

    print("Solution saved to '{}'".format(outfile))

## Will write to, e.g.: 'output/kn_bruteforce/<inputfilename>.output.234567'
# write_output(str([1, 2, 3]), prefix='kn_bruteforce', rnd=5)
