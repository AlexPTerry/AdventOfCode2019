from collections import defaultdict
import numpy as np

input_file = open('input/input_day10.txt', 'r').read().strip().split('\n')
astroid_positions = set()

for y, line in enumerate(input_file):
    for x, astroid in enumerate(line):
        if astroid == '#':
            astroid_positions.add(x+y*1j)

station_dict = {}
station_angles = {}

for station in astroid_positions:
    angle_set = set()
    angle_list = []

    for astroid in (astroid_positions - {station}):
        difference = astroid - station
        distance = difference.real**2 + difference.imag**2
        angle = np.angle(difference)

        angle_set.add(angle)
        angle_list.append((angle, distance))

        station_dict[station] = len(angle_set)
        station_angles[station] = angle_list

laser_position = max(station_dict, key=station_dict.get)
astroid_to_destroy = station_angles[laser_position]

angle_dict = defaultdict(lambda: [])
for astroid in astroid_to_destroy:
    angle_dict[astroid[0]].append(astroid[1])
    angle_dict[astroid[0]].sort()
angles_sorted = sorted(angle_dict.keys(), key=lambda theta: (np.pi/2 + theta) % (2*np.pi))

num_destroyed = 0
while len(angles_sorted) > 0:
    angles_copy = angles_sorted.copy()
    for angle in angles_copy:
        num_destroyed += 1
        if num_destroyed == 200:
            z = laser_position + angle_dict[angle][0]**0.5 * np.exp(1j*angle)
            print(round(z.real)*100 + round(z.imag))
        angle_dict[angle].pop(0)
        if len(angle_dict[angle]) == 0:
            angles_sorted.remove(angle)








