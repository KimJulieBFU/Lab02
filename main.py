from decimal import *
from math import factorial

def pi(n):
    D = Decimal(0)
    k = 0
    while k < n:
        D = D + (Decimal(-1) ** k) * (Decimal(factorial(6 * k)) / ((factorial(k) ** 3) * (factorial(3 * k))) * (13591409 + 545140134 * k) / (640320 ** (3 * k)))
        k += 1
    D = D * Decimal(10005).sqrt() / 4270934400
    D = D ** (-1)


    D=round(D,n)

    return D

print(pi(int(input())))
