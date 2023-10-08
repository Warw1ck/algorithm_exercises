the_elements = input().split(' ')
elements_should_be_there = [f'{x}' for x in range(1, len(the_elements)+2)]
missing_elements = filter(lambda x: x not in the_elements, elements_should_be_there)
print(f"Missing Elements: {' '.join(list(missing_elements))}")