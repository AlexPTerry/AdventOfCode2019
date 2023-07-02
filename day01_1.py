
import numpy as np
import pandas as pd

input_file = open('input/input_day01.txt', 'r').read().strip().split('\n')

total_fuel = 0
for mass in input_file:
    total_fuel += int(mass) // 3 - 2

print(total_fuel)







