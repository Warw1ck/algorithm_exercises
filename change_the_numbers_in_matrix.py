def change_the_symbols_in_matrix(matrix, game_symbol, my_x, my_y):
    initial_symbol = matrix[my_x][my_y]
    matrix[my_x][my_y] = game_symbol
    for new_coordinates in [[my_x+1, my_y], [my_x, my_y+1], [my_x-1, my_y], [my_x, my_y-1]]:
        new_x, new_y = new_coordinates
        if new_y == len(matrix[0]) or new_x == len(matrix):
            continue
        if matrix[new_x][new_y] == initial_symbol:
            matrix = change_the_symbols_in_matrix(matrix, game_symbol, new_x, new_y)


    return matrix



x, y = map(int, input().split(' '))
base_matrix = [input().split(' ') for i in range(x)]
base_game_symbol = input()
base_my_x, base_my_y = map(int, input().split(' '))
for element in change_the_symbols_in_matrix(base_matrix, base_game_symbol, base_my_x, base_my_y):
    print(''.join(element))

'''
INPUT:

5 6
s s u u s s
s u s s u s
u s s s s u
s u s s u s
s s u u s s
i
2 1

'''