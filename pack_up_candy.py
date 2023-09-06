def distribute_sweets(employees, k):
    total_sweets = sum(employees)
    if total_sweets % k != 0:
        return "Packaging is not possible!"

    sweets_per_pack = total_sweets // k
    packs = [[] for _ in range(k)]

    def backtrack(index):
        if index == len(employees):
            return True

        for i in range(k):
            if sum(packs[i]) + employees[index] <= sweets_per_pack:
                packs[i].append(employees[index])
                if backtrack(index + 1):
                    return True
                packs[i].pop()
        return False

    if backtrack(0):
        return packs
    else:
        return "Packaging is not possible!"


employees = list(map(int, input().split(", ")))
k = int(input())

result = distribute_sweets(employees, k)

if result == "Packaging is not possible!":
    print(result)
else:
    for i, pack in enumerate(result):
        print(f"Package {i + 1}: {', '.join(map(str, pack))}")