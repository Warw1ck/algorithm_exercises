the_elements = input().split(' ')
one_len_elements = list(filter(lambda x: the_elements.count(x) < 2, the_elements))
print(' '.join(one_len_elements))