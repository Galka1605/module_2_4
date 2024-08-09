numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
n = len(numbers)
primes = []
not_primes = []
for i in range(1, n):
    k = 0
    for j in range(1, numbers[i] + 1):
        if numbers[i] % j == 0:
            k += 1
    if k == 2:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print(primes)
print(not_primes)
