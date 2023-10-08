first_list = list(input().split(' '))
last_list = list(input().split(' '))


def myFun(x):
    if x in first_list:
        return True
    else:
        return False


same_element = list(filter(myFun, last_list))[0]
print(same_element)
