#!/bin/env python3
# Evan Widloski - 2019-12-01

import numpy as np

masses = np.loadtxt('input')

# %% part1

requirements = np.floor(masses / 3) - 2

print(np.sum(requirements))

# %% part2

extra_fuel = 0

for requirement in requirements:

    requirement = np.floor(requirement / 3) - 2

    while requirement > 0:

        extra_fuel += requirement
        print(requirement)
        requirement = np.floor(requirement / 3) - 2

print(np.sum(requirements) + extra_fuel)
