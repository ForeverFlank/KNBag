from knbag import *

print('Truth or Dare Example')
print('Players: Alice, Bob, Carol, Dave, Eve')
bag = KNBag(['Alice', 'Bob', 'Carol', 'Dave', 'Eve'], 2)
while input() == '':
    print(f'It\'s {bag.next()} turn!')