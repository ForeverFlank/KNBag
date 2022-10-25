from knbag import *

# generate 16 digits hexadecimal with no more than 2 same digits
for _ in range(10):
    print(''.join(KNBag('0123456789abcdef', 2).get(16)))