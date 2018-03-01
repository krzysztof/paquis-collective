import random
import sys
import os

from kn_utils import dist, write_output, ride_info

infile = sys.argv[1]
with open(infile, 'r') as fp:
    lines = [l.strip() for l in fp.readlines()]

# Rows, Cols, Fcars, Nrides, Bonus, Time
R, C, F, N, B, T = [int(x) for x in lines[0].split(' ')]

# Reading A lines into tuple of ints
rides = list(map(lambda x: tuple(map(int, x.split(' '))), lines[1: ]))

car_pos = [[0, 0] for _ in range(F)]
car_free_at = [0, ] * F

ride_dists = [dist(*r[:4]) for r in rides]

t = 0
car_choices = [[] for _ in range(F)]
ride_taken = [False, ] * N
score = 0
while t < T:
    for car_idx, (car_r, car_c) in enumerate(car_pos):
        choices = []

        if car_free_at[car_idx] > t:
            continue

        for ride_idx in range(len(rides)):
            if ride_taken[ride_idx]:
                continue
            rdist = ride_dists[ride_idx]
            possible, t_finish, bonus = ride_info(t, car_r, car_c, rides, ride_dists, ride_idx, T)
            if possible:
                choices.append((ride_idx, t_finish, rdist, bonus))
        # select min t_finish
        if choices:
            ride_idx, t_finish, rdist, bonus = min(choices, key=lambda x: (x[1], -x[2]))
            car_choices[car_idx].append(ride_idx)
            ride_taken[ride_idx] = True
            car_free_at[car_idx] = t_finish
            score += rdist + (B if bonus else 0)
            car_pos[car_idx] = rides[ride_idx][0], rides[ride_idx][1]
    #t = max(min(car_free_at), t + 1)
    t += 1

print("Score: {}".format(score))

car_choices2 = [list(map(str, [len(i), ] + i)) for i in car_choices]
data = "\n".join([" ".join(cc) for cc in car_choices2])
write_output(infile, data, prefix='kn_greedy1', rnd=5)
