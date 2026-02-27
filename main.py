from utils import get_fact, fib, nsd, is_prime

x = int(input())
y = int(input())

print("Factorial:", get_fact(x))

print("Fib:", fib(x))

print("nsd:", nsd(x,y))

print("prime:", is_prime(x))
