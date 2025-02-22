def detect_prime(n):
    if n < 2:
        return 0, []
    primes = [True]*n
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i,n,i):
                primes[j] = False

    arr = [i for i, v in enumerate(primes) if v]
    return sum(primes), arr

number, primes_arr = detect_prime(100)
print(number)
print(primes_arr)


def is_power_of_three(n: int) -> bool:
    if n < 1:
        return False
    while n % 3 == 0:
        n /= 3
    return n==1
print(is_power_of_three(242))