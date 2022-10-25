from random import shuffle

def shuffle_bag(lst, k=1):
        shuffled = lst * k                      # dupe list, then
        shuffle(shuffled)                       # shuffle it.
        return shuffled

class KNBag:
    def __init__(self, arg, k=1):
        if isinstance(arg, list):               # if arg is list,
            self.lst = arg                      # use it as bag list.
        elif isinstance(arg, int):              # if arg is int,
            self.lst = [x for x in range(arg)]  # generate list of numbers.
        elif isinstance(arg, str):              # if arg is string,
            self.lst = [c for c in arg]         # create a list out of their characters.
        else:
            raise Exception('ERROR: \'arg\' is neither an integer nor a list!')
        self.k = k
        self.n = len(self.lst)                  # n from size of bag
        self.shuffled = shuffle_bag(self.lst, self.k)   # initially rng'd list
        self.i = 0
    def next(self):                        # trying hard for optimization
        if self.i == self.n * self.k:
            self.shuffled = shuffle_bag(self.lst, self.k)
            self.i = 0
        self.i += 1
        return self.shuffled[self.i-1]
    def get(self, j=1):
        l = []
        for _ in range(j):
            if self.i == self.n * self.k:
                self.shuffled = shuffle_bag(self.lst, self.k)
                self.i = 0
            self.i += 1
            l.append(self.shuffled[self.i-1])
        return l
    def reset(self):
        self.shuffled = shuffle_bag(self.lst, self.k)
        self.i = 0

if __name__ == '__main__':
    # welcome start
    print('=<!! kn-Bag RNG by jsudo !!>=\n')
    print('  You are currently running  ')
    print('  this program as __main__.  ')
    print('   Input \'help\' for help   ')
    print(' or leave empty to continue.\n')
    # welcome end
    if input('>> ') == 'help':
        # help start
        print('\nApologies for furthur grammartical mistakes or confusion, if I made any.')
        print('[whisper] but I will probably not fix it kekw')
        print('\n:: INTRODUCTION AND MOTIVATION ::\n')
        if input('[keep pressing enter to continue]\n[or input \'skip\' to skip to the how-to] ') != 'skip':
            print('\nThis is kn-Bag random generation system.')
            print('This system is guaranteed to delivers evenly distributed outputs.')
            input() # to prevent user from wall of text

            print('This random generation method is heavily inspired by Tetris \'7-Bag\'')
            print('system that evenly gives all randomized 7 tetrominoes in every 7 pieces you get.')
            # implement your own system because pro
            print('For example: ')
            for i in range(3):
                print(KNBag('IJLSZOT').get(7), end=' \ ')
            print('...')
            input()

            print('Later, \'Tetr.io\' implemented \'14-Bag\' system which gives you all randomized 7')
            print('tetrominoes twice every 14 pieces you get.')
            print('For example: ')
            for i in range(2):
                print(KNBag('IJLSZOT', 2).get(7), end=' \ ')
            print('...')
            print('In this case, the \'loop size\' of the bag is 2, since you got 2 pieces every 7*2 = 14 times.')
            input()

            print('Those techniques mentioned above gave me an idea -- to make a general-purpose')
            print('random generation system that randomize any data for any \'loop size\'.')
            print('kn-Bag works by just change IJLSZOT to something else you want, and make a')
            print('configurable \'loop size\'')
            input()

            print('This is how it kn-Bag gets its name -- k for \'loop size\',')
            print('and \'n\' for size of loop bag.')
            print('(For 7-bag, the \'k\' value is 1 and for 15-bag, the \'k\' value is 2.')
            print('Both have \'n\' value of 7.)')
            input()
            
            print('That\'s all for introduction.\n')
        
        print(':: HOW TO USE\n')
        if input('[keep pressing enter to continue]\n[or input \'skip\' to skip to the program] ') != 'skip':
            print('\nYou will be asked to enter \'n\' and \'k\' as a positive integer each.')
            print('\'n\' is for size of list and \'k\' for loop size.\n(see above from introduction)')
            input()

            print('Later, you will be asked to enter name or not. If yes (\'y\'), input name of items for n times.')
            print('If not (\'n\'), the program will use list of integers in interval [1,n] instead.')
            input()

            print('After all of that, keep pressing enter (empty input) to generate randomized items from kn-Bag.')
            print('If you wish to exit, type something (input is not empty) before enter.')
            input()

            print('For implementation, please read the README or see example files.')
            print('That\'s all for how-to.')
            input()
        # help end
    n = int(input('n = '))
    k = int(input('k = '))
    name = []
    b = input('Input name? [Y/n] ').lower() == 'y'
    if b:
        for _ in range(n):
            name.append(input())

    print(' ++! START of RNGesus !++ ')
    inp = name if b else n
    bag = KNBag(inp, k)
    while input() == '':
        print(bag.next() + (1 if not b else ''), end='')