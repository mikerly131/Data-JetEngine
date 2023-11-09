#!/usr/bin/env python3

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(22):
    result = die.roll()
    results.append(result)

print(results)