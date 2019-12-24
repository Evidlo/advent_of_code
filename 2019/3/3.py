#!/bin/env python3
# Evan Widloski - 2019-12-02

line1, line2 = open('input', 'r').read().split('\n')

# line1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
# line2 = 'U62,R66,U55,R34,D71,R55,D58,R83'

# line1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
# line2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

# line1 = 'R8,U5,L5,D3'
# line2 = 'U7,R6,D4,L4'

# line1 = 'R10,U20'
# line2 = 'U10,R20'

# line1 = 'U10'
# line2 = 'R10'

# line1 = 'U10'
# line2 = 'L10'

# line1 = 'R10'
# line2 = 'D10'

# line1 = 'D10'
# line2 = 'L10'

def parse_line(line):

    # x pos, y pos, accumulated wire len
    x, y, w = 0, 0, 0

    points = [(x, y)]

    # loop through line commands
    for command in line.split(','):

        direction = command[0]
        distance = int(command[1:])

        w += distance

        if direction == 'U':
            y += distance
        if direction == 'D':
            y -= distance
        if direction == 'R':
            x += distance
        if direction == 'L':
            x -= distance

        points.append((x, y, w))

    return points

points1 = parse_line(line1)
points2 = parse_line(line2)

intersections = []
m_distances = []
w_distances = []
for s1, e1 in zip(points1[:-1], points1[1:]):
    for s2, e2 in zip(points2[:-1], points2[1:]):

        # order start/end points by left-downmost then up-rightmost
        ld1, ur1 = (s1, e1) if s1[0] < e1[0] or s1[1] < e1[1] else (e1, s1)
        ld2, ur2 = (s2, e2) if s2[0] < e2[0] or s2[1] < e2[1] else (e2, s2)

        # check for intersection
        if (ld2[0] <= ur1[0] and ur2[0] >= ld1[0] and ld2[1] <= ur1[1] and ur2[1] >= ld1[1]):
            x, y = max(ld1[0], ld2[0]), max(ld1[1], ld2[1])
            intersections.append((x, y))
            m_distances.append(x + y)
            w_distances.append(
                e1[2] - abs(e1[0] - x) - abs(e1[1] - y) +
                e2[2] - abs(e2[0] - x) - abs(e2[1] - y)
            )

# remove centrol port intersection
m_distances = m_distances[1:]
w_distances = w_distances[1:]

print('min mann. distance:', min(m_distances))
print('min wire distance:', min(w_distances))
