numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def find_largest_subarray(numbers):
    number_combination = [[numbers[k] for k in range(n, i)] for n in range(len(numbers)) for i in range(n, len(numbers))]
    print(sorted(number_combination, key=lambda x: sum(x))[-1])



find_largest_subarray(numbers)