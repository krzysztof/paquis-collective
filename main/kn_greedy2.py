import random
import sys
import os

from kn_utils import dist, write_output, ride_info


def save_data(car_choices, prefix='kn_out'):
    car_choices2 = [list(map(str, [len(i), ] + i)) for i in car_choices]
    data = "\n".join([" ".join(cc) for cc in car_choices2])
    write_output(infile, data, prefix=prefix, rnd=5)

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
rides_idxs = dict((i, r) for i, r in enumerate(rides))
score = 0

for car_idx in range(F):
    car_r, car_c = 0, 0
    t = 0
    while t < T:
        print("Car:", car_idx, F)
        print("T:", t, T)
        print("Rides:", len(rides_idxs))
        choices = []
        for ride_idx, ride in rides_idxs.items():
            ride_r0, ride_c0, ride_r1, ride_c1, t_start, t_end = ride
            rdist = ride_dists[ride_idx]
            possible, t_finish, arrive_dist, bonus = ride_info(t, car_r, car_c, ride, rdist, T)
            if possible:
                choices.append((ride_idx, t_finish, arrive_dist, rdist, bonus))
        if choices:
            #ride_idx, t_finish, arrive_dist, rdist, bonus = min(choices, key=lambda x: (x[1], (-x[3]-x[4])))
            ride_idx, t_finish, arrive_dist, rdist, bonus = min(choices, key=lambda x: (x[1], (-x[3]-x[4])))
            car_choices[car_idx].append(ride_idx)
            t = t_finish
            score += rdist + (B if bonus else 0)
            car_r, car_c = rides_idxs[ride_idx][2: 4]
            del rides_idxs[ride_idx]
        else:
            t = T
print(score)
#print(car_choices)

save_data(car_choices, prefix='kn_greedy2')
