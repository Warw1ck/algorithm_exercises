the_elements = input().split(' ')

the_elements = sorted(the_elements, key= lambda x: the_elements.count(x))
print(f"The unique: {' '.join(the_elements[:1])}")
print(f"The other: {' '.join(set(the_elements[1:]))}")

