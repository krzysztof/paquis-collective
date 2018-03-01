import random
import sys
import os

def dist(r0, c0, r1, c1):
    return abs(r0-r1) + abs(c0-c1)

def write_output(infile, data, prefix="", rnd=0):
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


def ride_info(t, car_r, car_c, ride, rdist, T):
    ride_r0, ride_c0, ride_r1, ride_c1, t_start, t_end = ride
    car_to_ride_dist = dist(car_r, car_c, ride_r0, ride_c0)
    t_arrive = t + car_to_ride_dist
    t_wait = max(t_start - t_arrive, 0)
    t_ride_start = t_arrive + t_wait

    t_finish = t_ride_start + rdist
    # Can you make the trip?
    can_make_it = t_finish < t_end
    bonus = t_arrive == t_start
    return can_make_it, t_finish, car_to_ride_dist, bonus
