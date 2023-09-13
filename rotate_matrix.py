def rotate_matrix(matrix):
    result = [[] for _ in range(len(matrix))]
    matrix = matrix[::-1]
    for el in matrix:
        for i in range(len(el)):
            result[i].append(el[i])
    return result


print(rotate_matrix([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
