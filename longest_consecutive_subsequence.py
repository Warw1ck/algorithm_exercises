numbers = [3, 4, 5, 1, 2, 8, 9, 10, 11, 12, 7]


def longest_consecutive_subsequence(numbers):
    subsequence = []
    i = 0
    new_sub = True
    while i<len(numbers):
        if new_sub:
            subsequence.append([numbers[0]])


    return subsequence



print(longest_consecutive_subsequence(numbers))