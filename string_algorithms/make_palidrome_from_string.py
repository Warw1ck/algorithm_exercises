from math import ceil


def make_palindrome(word:str):
    palindrome_word = None
    if len(word) % 2 == 0:
        print(word[:round(len(word)/2)])
        palindrome_word = word[:round(len(word)/2)] + word[:round(len(word)/2)][::-1]
    else:
        palindrome_word = word[:len(word)//2] +word[len(word)//2] + word[:len(word)//2][::-1]
    return palindrome_word

word1 = 'abcdifg'
print(make_palindrome(word1))

