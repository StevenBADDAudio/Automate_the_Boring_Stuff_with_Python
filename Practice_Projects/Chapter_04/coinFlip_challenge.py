import random

numberOfStreaks = 0
sample = []

for experimentNumber in range(10000):
    flips_100 = []

    # Code that creates a list of 100 'heads' or 'tails' values.
    for flip in range(100):
        if random.randint(0, 1) == 0:
            flips_100.append('T')
        else:
            flips_100.append('H')
    sample.append(flips_100)

# Code that checks if there is a streak of 6 heads or tails in a row.
count = 0
for experimentNumber in range(10000):
    for flip in range(100):

        if sample[experimentNumber][flip:(flip + 6)] == ['H', 'H', 'H', 'H', 'H', 'H']:
            count += 1
            break
        elif sample[experimentNumber][flip:(flip + 6)] == ['T', 'T', 'T', 'T', 'T', 'T']:
            count += 1
            break
        else:
            continue
       
numberOfStreaks = count / 10000 * 100

print(f'Chance of streak: {numberOfStreaks}%')
