import random
import sys
import functools
import os


class ride:
    def __init__(self, a, b, x, y, s, f):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f

    def value(self):
        return abs(self.a - self.x) + abs(self.b - self.y) + B


def compare(r1, r2):
    if r1.value() < r2.value():
        return -1
    elif r1.value() > r2.value():
        return 1
    else:
        return 0


infile = sys.argv[1]
with open(infile, 'r') as fp:
    lines = [l.strip() for l in fp.readlines()]


# Some common follow-ups:
# Usually first line specifies some numbers A, B, C, D, etc.:
R, C, F, N, B, T = [int(x) for x in lines[0].split(' ')]

# Reading A lines into tuple of ints
rides = list(map(lambda x: tuple(map(int, x.split(' '))), lines[1: ]))
rides = [ride(*i) for i in rides]
sorted_rides = sorted(rides, key=functools.cmp_to_key(compare))

import ipdb
ipdb.set_trace()

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
