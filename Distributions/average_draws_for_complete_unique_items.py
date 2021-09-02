"""
From Sheldon Ross's Introduction to Probability
Chapter 2, #42 of the 12th Edition

Suppose that each coupon obtained is, independent of what has been previously
obtained, equally likely to be any of m different types. Find the expected number
of coupons one needs to obtain in order to have at least one of each type.

Conclusion:
E[X] = m ln(m) where m is number of coupons
"""

import random as rand

def setup_sim(num_coupons, trials=10000):
    avg = []
    for trial in range(trials):
        i = sim(num_coupons)
        avg.append(i)
    return sum(avg)/trials

def sim(num_coupons):
    x = list(range(1, num_coupons + 1))
    chosen = rand.choice(x)
    drawn = {chosen: 1}
    key_len = len(drawn.keys())
    i = 1
    while key_len != num_coupons:
        i += 1
        chosen = rand.choice(x)
        if chosen not in drawn.keys():
            drawn[chosen] = 1
            key_len = len(drawn.keys())
    return i

for i in range(1, 11):
    print(i, setup_sim(i))