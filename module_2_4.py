numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    if num == 1:
        continue
    isPrime = True
    for num2 in range(2, num):
        if num % num2 == 0:
            isPrime = False
    if isPrime:
        primes.append(num)
    else:
        not_primes.append(num)

print("primes: ", primes)
print("not primes: ", not_primes)
