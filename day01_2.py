
import numpy as np
import pandas as pd

input_file = open('input/input_day01.txt', 'r').read().strip().split('\n')

total_fuel = 0
for mass in input_file:
    subtotal_fuel = int(mass) // 3 - 2

    additional_fuel = subtotal_fuel // 3 - 2
    while additional_fuel >= 0:
        subtotal_fuel += additional_fuel
        additional_fuel = additional_fuel // 3 - 2

    total_fuel += subtotal_fuel

print(total_fuel)








