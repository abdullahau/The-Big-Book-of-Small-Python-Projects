import datetime
from random import choices

print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

print('How many birthdays shall I generate? (Max 100)')
print()

num = int(input('> '))
print()

today = datetime.date.today().toordinal()
birthdays = [datetime.date.fromordinal(i).strftime('%b %#d') for i in choices(range(1, today), k=num)]
print(f'Here are {num} birthdays:')
print(', '.join(birthdays))
print()

seen = set()
dupes = [x for x in birthdays if x in seen or seen.add(x)] 
print('In this simulation, multiple people have a birthday on the following dates:', ', '.join(dupes))
print()

print('Generating', num, 'random birthdays 100,000 times...')
input('Press Enter to begin...')
print('Let\'s run another 100,000 simulations.')

result = 0
print(f'{0} simulations run...')
for j in range(100_000):
    birthdays = choices(range(1,366),k=num)
        
    if len(birthdays) != len(set(birthdays)):
        result += 1

    if (j+1) % 10_000 == 0:
        print(f'{j+1} simulations run...')

probability = round(result / 100_000 * 100, 2)
print('Out of 100,000 simulations of', num, 'people, there was a')
print('matching birthday in that group', result, 'times. This means')
print('that', num, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')