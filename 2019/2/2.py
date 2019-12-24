#!/bin/env python3
# Evan Widloski - 2019-12-01

def compute(noun, verb):

    intcodes = list(map(int, open('input', 'r').read().split(',')))

    intcodes[1] = noun
    intcodes[2] = verb

    index = 0

    while True:

        if intcodes[index] == 1:
            intcodes[intcodes[index + 3]] = (
                intcodes[intcodes[index + 1]] +
                intcodes[intcodes[index + 2]]
            )
            index += 4
        elif intcodes[index] == 2:
            intcodes[intcodes[index + 3]] = (
                intcodes[intcodes[index + 1]] *
                intcodes[intcodes[index + 2]]
            )
            index += 4
        elif intcodes[index] == 99:
            break

    return intcodes


print(compute(12, 2)[0])

# %% part2

from itertools import product

for noun, verb in product(range(100), range(100)):

    result = compute(noun, verb)[0]

    if result == 19690720:

        print(100 * noun + verb)
