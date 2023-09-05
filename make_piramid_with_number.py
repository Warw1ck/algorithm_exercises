def create_num_piramid(piramid_number):
    result = []
    for i in range(piramid_number, 0, -1):
        row = f"{' '*(piramid_number-i)}{''.join([str(n) for n in range(1, i)])}{i}{''.join([str(n) for n in range(1, i)][::-1])}"
        result.append(row)
    return '\n'.join(result)

print(create_num_piramid(int(input())))