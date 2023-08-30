def find_digital_root_of_number(main_number):
    digital_root = main_number
    while digital_root >= 10:
        digital_root = sum(list(map(lambda x: int(x), [*str(digital_root)])))
    print(digital_root)

find_digital_root_of_number(285)