import random
max_number = 1000
min_number = 1
answer = random.randint(min_number, max_number)


def gues(x):
    if x == answer:
        return 0
    elif x > answer:
        return -1
    else:
        return 1


last_number = 0
my_gues = 500

while True:
    gues_number = gues(my_gues)
    mid = (my_gues - last_number)//2
    if gues_number > 0:
        last_number = my_gues
        my_gues += mid

    elif gues(my_gues) < 0:
        my_gues -= mid

    else:
        print(f'You won! With number {my_gues}')
        break
