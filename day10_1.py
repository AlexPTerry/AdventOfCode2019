from collections import defaultdict

input_file = open('input/input_day10.txt', 'r').read().strip().split('\n')
astroid_positions = set()

for y, line in enumerate(input_file):
    for x, astroid in enumerate(line):
        if astroid == '#':
            astroid_positions.add(x+y*1j)

station_dict = {}

for station in astroid_positions:
    gradient_set = set()

    for astroid in (astroid_positions - {station}):
        difference = astroid - station
        distance = difference.real**2 + difference.imag**2
        gradient_unrounded = difference / distance**0.5
        gradient = round(gradient_unrounded.real, 3) + round(gradient_unrounded.imag, 3)*1j

        gradient_set.add(gradient)

        station_dict[station] = len(gradient_set)

print(max(station_dict, key=station_dict.get), max(station_dict.values()))


