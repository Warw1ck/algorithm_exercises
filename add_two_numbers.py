def addTwoNumbers(l1, l2):
    new_number = str(int(''.join(list(map(str, l1)))) + int(''.join(list(map(str, l2)))))
    return [ch for ch in new_number][::-1]

print(addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))