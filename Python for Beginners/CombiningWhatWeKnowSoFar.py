from decimal import Decimal, getcontext
import math


def calc(n):
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)
    k = 0
    for k in range(n):
        t= (Decimal(-1)**k)*(math.factorial(Decimal(6)*k))*(13591409 + 545140134*k)
    return str(pi)

calc(1)