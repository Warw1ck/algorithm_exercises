import functools


def find_missing_number(nums):
    number_sum_should_be = functools.reduce(lambda a, b: a+b, range(max(nums)+1))
    return number_sum_should_be - sum(nums)

print(find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))