#! /usr/bin/env python3


def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(10):
    print('T-minus', x)


# for loop is really like this

_iter = iter(obj)            # get iterator object
while 1:
    try:
        x = _iter.next()     # get next item
    except StopIteration:    # no more items
        break

# any object that supports iter() and next() is said to be 'iterable'

a = [1,2,3,4]
b = [2*x for x in a]
c = (2*x for x in a)
