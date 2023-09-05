def show_prime(start, end):
    all_prime = [number for number in range(start-1, end+1) if not [deletels for deletels in range(2, number) if number%deletels==0] and number > 1]
    return all_prime
start = int(input())
end = int(input())
prime = show_prime(start, end)
print(f"{' '.join(map(str, prime))}\nThe total number of prime numbers between {start} to {end} is {len(prime)}")