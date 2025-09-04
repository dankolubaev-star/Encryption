from math import gcd

def _isprime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        if n == 2:
            return True 
        else:
            return False
i = 3
while i * i <= n: 
    if n % i == 0:
        return False
    i = i + 2
    return True

def _nextprime(x):
    if x <= 2:
        return 2
    if x % 2 == 0:
        x += 1
    while not _isprime(x):
        x += 2 
    return x

def _inverse(a, m):
    x0, x1 = 1, 0
    r0, r1 = a, m 
while r1 !=