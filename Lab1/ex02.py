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


def twoPrimesFormingN(n):
    p1 = 2
    p2 = n - 2
    while not (isPrime(p1) and isPrime(p2)):
        p1 += 1
        p2 -= 1
    return {'p1': p1, 'p2': p2}

def printToConsoleTwoPrimesFormingN(n):
    print(twoPrimesFormingN(n)['p1'], twoPrimesFormingN(n)['p2'])


printToConsoleTwoPrimesFormingN(58)
