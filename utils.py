import math


def get_fact(x):
    return math.factorial(x)

def nsd(x,y):
    return math.gcd(x, y)

def fib(n):
    a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
