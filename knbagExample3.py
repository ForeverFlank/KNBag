from knbag import *

# reset example
# pray for luck and you will see
# the second line might not generate a valid bag
print('Without reset')
a = KNBag('ABCD', 2)
print(' '.join(a.get(2)))
print(' '.join(a.get(8)))

# first 2 chars of the second line might 'overlap' with the first line
print('With reset')
b = KNBag('ABCD', 2)
print(' '.join(b.get(6)))
b.reset() # bag reset here
print(' '.join(b.get(8)))