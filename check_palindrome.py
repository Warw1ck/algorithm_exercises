from math import floor


def check_palindrome(element):
    odd_or_even_plus = 0
    if len(element) % 2 == 1:
        odd_or_even_plus += 1
        
    first_part = element[:floor(len(element)//2)]
    second_part = element[floor((len(element) // 2)+odd_or_even_plus):][::-1]

    if first_part == second_part:
        print('Palindrome True')
    else:
        print('Palindrome False')


check_palindrome('abcbba')