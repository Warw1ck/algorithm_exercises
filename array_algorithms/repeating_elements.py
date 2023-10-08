import numpy as np

the_elements = input().split(' ')
one_len_elements = filter(lambda x: the_elements.count(x) > 1, the_elements)
print(' '.join(np.unique(list(one_len_elements))))