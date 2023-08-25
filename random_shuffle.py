from numpy.random import rand


def my_shuffle(*args):
    new = list(args)
    the_rand = rand(len(args))
    for index, element in enumerate(args):
        new.remove(element)
        num = round(the_rand[index]*10)
        new.insert(num, element)
    return new


def my_shuffle2(*args):
    new = list(args)
    the_rand = rand(len(args))
    new = [args[round(x*10)]for x in the_rand]
    return new


print(my_shuffle(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
