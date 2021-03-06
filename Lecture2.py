## Names bind to values in order to use them later.
## Def is a binder to create our own functions

import operator

def square(x):
  return operator.mul(x, x)

square(11)


def sum_squares(x, y):
  return square(x) + square(y)



## instead of defining an area for example.....
radius = 10
pi = 3.14
def area():
  return pi * radius * radius

area()


## primitives
number = 1
name = job
string = "david"

##call expressions
max(2, 3)


from operator import mul
def square(x):
    return mul(x, x)

square(-2)