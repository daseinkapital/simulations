"""
From Sheldon Ross's Introduction to Probability
Chapter 2, #39 of the 12th Edition

An urn has 8 red and 12 blue balls. Suppose that balls are chosen at random
and removed from the urn, with the process stopping when all the red balls have
been removed. Let X be the number of balls that have been removed when the
process stops.
(a) Find P(X=14)
(b) Find the probability that a specified blue ball remains in the urn.
(c) Find E[X]

Conclusion:
(a) ((8 chose 7)(12 choose 6))/(20 chose 13) * (1/7) which is ~0.0136
(b) Probability is the probability that ball j of m blue balls is still in the urn multiplied by the probability of that event occurring
(c) sum(i * P(X_i = i)) for i 8 to 20 which is ~18.6
"""

import random as rand

def setup_sim_a(trials=10000):
    results = {i: 0 for i in range(8,21)}
    for trial in range(trials):
        i = sim_a()
        results[i] += 1
    for key in results.keys():
        results[key] /= trials
    return results


def sim_a():
    balls = list(range(1,21))
    found = []
    found_len = 0
    success = {i:1 for i in range(1,9)}
    chosen = rand.choice(balls)
    balls.remove(chosen)
    i = 1
    while i < 20:
        if chosen in success.keys():
            found.append(chosen)
            found_len = len(found)
            if found_len == 8:
                return i
        i += 1
        chosen = rand.choice(balls)
        balls.remove(chosen)    
    return i

def part_b():
    results = setup_sim_a(1000000)
    total = 0
    for key, val in results.items():
        total += (20-key)*val/12
    return total

def part_b_theoretical_approach():
    expected = []
    for i in range(8,21):
        blues_remaining = 20-i
        probability = (choose(8,7)*choose(12, 12 - blues_remaining))/(choose(20,i-1) * (20-(i-1)))
        # print(probability)
        expected.append((20-i)*probability/12)
    return sum(expected)

def part_c():
    results = setup_sim_a(1000000)
    total = 0
    for key, val in results.items():
        total += key*val
    return total

def part_c_theoretical_approach():
    expected = []
    for i in range(8,21):
        blues_remaining = 20-i
        probability = (choose(8,7)*choose(12, 12 - blues_remaining))/(choose(20,i-1) * (20-(i-1)))
        # print(probability)
        expected.append(i*probability)
    return sum(expected)

def choose(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print("Distribution")
print(setup_sim_a(1000000))

print("Part A")
print(setup_sim_a(1000000)[14])

print("Part B - Method 1 (Theoretical)")
print(part_b_theoretical_approach())
print("Part B - Method 2 (Simulation)")
print(part_b_theoretical_approach())

print("Part C - Method 1 (Theoretical)")
print(part_c_theoretical_approach())
print("Part C - Method 2 (Simulation)")
print(part_c())