def number_stairs(stairs):
    first_number = 1
    second_number = 2

    for i in range(2, stairs):
        second_number = first_number + second_number
        first_number = i

    return second_number


def climb_stairs(n, current=[]):
    if n == 0:
        print(current)
    elif n >= 2:
        climb_stairs(n - 2, current + ["2"])
        climb_stairs(n - 1, current + ["1"])
    else:
        climb_stairs(n - 1, current + ["1"])






