import math


def isPrime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        i = 2
        while i <= int(math.sqrt(n)):
            if n % i == 0:
                return False
            else:
                i += 1
        return True


def primeList(N):
    """
    returns list of primes less than or equal to N
    """
    prime_list = []
    n = 2
    while n <= N:
        if isPrime(n):
            prime_list.append(n)
            n += 1
            continue
        else:
            n += 1
            continue
    return prime_list


print(primeList(23))