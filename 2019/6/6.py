#!/bin/env python3
# Evan Widloski - 2019-12-07

input = 'COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L'
input = open('input', 'r').read()

orbits = []
secondaries = []
for o in input.split('\n'):
    primary, secondary = o.split(')')
    orbits.append((primary, secondary))
    secondaries.append(secondary)

nodes = {}

for primary, secondary in orbits:

    # need to build tree from top to bottom
    # if an orbit comes out of order, deal with it later

    if primary in nodes:
        nodes[secondary] = nodes[primary] + 1
    elif primary in secondaries:
        orbits.append((primary, secondary))
    else:
        nodes[secondary] = 1
        nodes[primary] = 0

print('checksum:', sum(nodes.values()))


