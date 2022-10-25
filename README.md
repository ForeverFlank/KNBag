# KNBag
Even distribution random generation system inspired by Tetris and TETR.io (from 7-Bag and 14-Bag).

For Python.

## What is this?
~~Prepare to get confused by my grammar and my English skills lol~~

This random generation system gives even distribution outputs. You will guaranteed to get *k* of each items in *n* in every *kn* times.

Imagine you have 4 marbles *(red, green, blue and white)*, put them in the bag, randomly pick one out from the bag, repeat 4 times until the bag runs out of marbles, then put back all marbles inside the bag again (and repeat again and again). In this case, *n*=4 and *k*=1.

    Example : R G W B / W G B R / W R B G / G R B W ... (assume '/' are invisible)

Now imagine you have 8
 marbles *(red, green, blue and white, 2 marbles for each color)*, do the same thing as above: put them in the bag, pick one out and repeat. In this case, *n*=4 (there are still 4 colors) and *k*=2 (2 marbles each).
 

    Example : R B W R G B W G / B W W G R B R G / ... ('/' are still invisible)

*kn-Bag* is when you put *n* things in the bag with *k* items of each item in *n*.

~~This is cool for Truth or Dare lol~~

## How to use

### To create a new 'bag', use

    bag = KNBag(arg, k)

`arg` : Items to be randomized - can be `list`, `int`, or `string`
If type is

 - `list` : the list will be used as the bag
 - `int` : list of integers in interval [0, `arg`-1] will be used as the bag
 - `string` : list of characters in the string will be used as the bag

### To get the result of the next item, use
    bag.next()
The function will return the next item of the bag.
### To get the list of next incoming items, use
	bag.get(j)
The function will return list of next `j` items of the bag. (`j` must be a positive integer)
### To reset the bag, use
	bag.reset()
The function will reset the bag (a.k.a "put everything back to the bag and restart again").
