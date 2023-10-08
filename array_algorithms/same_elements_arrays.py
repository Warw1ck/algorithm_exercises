def find_same_numbers(array1, array2):
    return ', '.join(map(lambda x: str(x), set(filter(lambda x: x in array1, array2))))

print(find_same_numbers([1, 2 , 3, 4, 5], [ 2, 6, 8, 9, 3]))
