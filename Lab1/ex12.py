def digitsOfNToArray(n):
    digits = [0] * 10
    while n > 0:
        digits[int(n % 10)] += 1
        n = n / 10
    return digits


def areP(n1, n2):
    i = 0
    digitsOfN1 = digitsOfNToArray(n1)
    digitsOfN2 = digitsOfNToArray(n2)
    while i < 10:
        if (digitsOfN1[i] != 0 and digitsOfN2[i] == 0) or (digitsOfN1[i] == 0 and digitsOfN2[i] != 0):
            return False
        i += 1
    return True


n1 = input("n1 = ")
n2 = input("n2 = ")
print(areP(int(n1), int(n2)))
