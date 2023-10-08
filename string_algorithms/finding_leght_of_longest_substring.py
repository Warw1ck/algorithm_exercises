def find_longest_substring_length(word):
    chars = 0
    new = 0
    for i in range(len(word)):
        if word[i] in word[new:i]:
            new = i
        if i != len(word) -1:
            chars = max(chars, find_longest_substring_length(word[i+1:len(word)]))
        chars = max(chars, i - new +1)

    return chars


print(find_longest_substring_length("bhhoejpnsoqioadvynqrbo"))
