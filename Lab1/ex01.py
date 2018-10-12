import math


def isPrime(n):
    if n == 1 or n == 0:
        return False
    if n % 2 == 0 and n != 2:
        return False
    d = 3
    while d <= math.floor(math.sqrt(n)):
        if n % d == 0:
            return False
        d += 2
    return True


def firstPrimeGreaterThan(n):
    n += 1
    while not isPrime(n):
        n += 1
    return n


userInput = input("give a number")
print(firstPrimeGreaterThan(int(userInput)))
