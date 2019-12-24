#!/bin/env python3
# Evan Widloski - 2019-12-07

# input = 'COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nI)SAN\nK)YOU'
input = open('input', 'r').read()

parents = {}

for orbit in input.split('\n'):
    primary, secondary = orbit.split(')')

    parents[secondary] = primary

def get_limb(secondary):

    limb = []
    parent = parents[secondary]
    while parent != 'COM':
        limb.append(parent)
        parent = parents[parent]

    return limb

limb_you = get_limb('YOU')
limb_san = get_limb('SAN')

# traverse limbs backwards to find last common point
common = 1
for node_a, node_b in zip(reversed(limb_you), reversed(limb_san)):
    if node_a != node_b:
        break
    common += 1

print('transfers:', (len(limb_you) - common + 1) + (len(limb_san) - common + 1))
