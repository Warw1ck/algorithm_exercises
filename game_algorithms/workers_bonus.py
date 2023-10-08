from functools import reduce
all_bonus = 0
while True:
    command = input()
    if command == 'stop':
        break

    tasks = list(map(int, input().split(', ')))
    bonus = sum([reduce(lambda x, y: x*y, [*tasks[:tasks.index(n)], *tasks[tasks.index(n)+1:]]) for n in tasks])
    all_bonus += bonus
    print(f"{command} has a bonus of {bonus} lv.")


print(f"The amount of all bonuses is {all_bonus} lv.")