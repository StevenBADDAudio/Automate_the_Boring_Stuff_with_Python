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

for experimentNumber in range(10000):
    count_H = 0
    count_T = 0
    for flip in range(100):

        if sample[experimentNumber][flip] == 'H':
            count_H += 1
            count_T = 0
        elif sample[experimentNumber][flip] == 'T':
            count_T += 1
            count_H = 0
        if count_H == 6 or count_T == 6:
            count_H = 0
            count_T = 0
            numberOfStreaks += 1

#print(count)        
#numberOfStreaks = count / 10000

#print(sample[1])
#print(sample[1][97:(97+5)])

print('Chance of streak:  %s%%' % (numberOfStreaks / 100))