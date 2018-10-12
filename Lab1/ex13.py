def numberOfPrimeDivisors(n):
    if n == 1:
        return 1
    d = 2
    primeDivisors = 0
    while n > 1:
        if n % d == 0:
            while n % d == 0:
                n = n / d
            primeDivisors += 1
        else:
            d += 1
    return primeDivisors


def nthNumberInPrimeDivisorsSequence(n):
    currentIndex = 1


print(numberOfPrimeDivisors(1))