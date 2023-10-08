numbers = [3, 4, 5, 1, 2, 8, 9, 10, 11, 12, 7]


def longest_consecutive_subsequence(numbers):
    subsequence = []
    i = 0
    new_sub = True
    while i < len(numbers):
        if new_sub:
            subsequence.append([numbers[i]])
            new_sub = False
            i += 1
            continue
        if numbers[i - 1] + 1 == numbers[i]:
            subsequence[-1].append(numbers[i])
        else:
            new_sub = True
            continue
        i += 1

    return sorted(subsequence)[-1]


print(longest_consecutive_subsequence(numbers))
