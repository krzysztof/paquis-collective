import random
import sys
import os

infile = sys.argv[1]
with open(infile, 'r') as fp:
    lines = [l.strip() for l in fp.readlines()]
# Some common follow-ups:
# Usually first line specifies some numbers A, B, C, D, etc.:
R, C, F, N, B, T = [int(x) for x in lines[0].split(' ')]

# Reading A lines into tuple of ints
rides = list(map(lambda x: tuple(map(int, x.split(' '))), lines[1: ]))

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
