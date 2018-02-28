import random
import sys
import os

infile = sys.argv[1]
with open(infile, 'r') as fp:
    lines = [l.strip() for l in fp.readlines()]
# Some common follow-ups:
# Usually first line specifies some numbers A, B, C, D, etc.:
# A, B, C, D = [int(x) for x in lines[0].split(' ')]

# Reading A lines into tuple of ints
# AA = list(map(lambda x: tuple(map(int, x.split(' '))), lines[1: A+1]))

# Reading B lines after taht into tuple of ints
# BB = list(map(lambda x: tuple(map(int, x.split(' '))), lines[A+1: A+B+1]))

# Reading C lines after taht into tuple of ints
# CC = list(map(lambda x: tuple(map(int, x.split(' '))), lines[A+B+1: A+B+C+1]))

# Reading all input into an array (e.g. A x B)
# arr = lines[1:]  # The rest of input


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
