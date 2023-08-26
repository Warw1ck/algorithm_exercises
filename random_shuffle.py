from math import ceil
from random import randint
from numpy.random import rand


def my_shuffle(*args):
    new = list(args)
    for index, element in enumerate(args):
        rand_number = randint(0, len(new)-1)
        new.remove(element)
        new.insert(rand_number, element)
    return new

def my_shuffle2(*args):
    new = list(args)
    for index in range(len(new)):
        rand_number = randint(0, len(new)-1)
        new[index], new[rand_number] = new[rand_number], new[index]
    return new


print(my_shuffle(1, 2, 3, 4, 5, 6, 7, 8))
