

def check_operations_numbers_for_transformation_name(name, reference):
    reference_chars = [ch for ch in reference]
    name_chars = [ch for ch in name]
    fixed_name = ['' for _ in reference]
    transformation = False
    for i in range(len(name)):
        first_char = name_chars.pop()
        if first_char not in reference_chars:
            break
        fixed_name[reference_chars.index(first_char)] = first_char
        if fixed_name == reference_chars:
            return f'The minimum operations required to convert "{name}" to "{reference}" are {i}'

    if not transformation:
        return 'The name cannot be transformed!'


input_name = input()
input_reference = input()
print(check_operations_numbers_for_transformation_name(input_name, input_reference))




