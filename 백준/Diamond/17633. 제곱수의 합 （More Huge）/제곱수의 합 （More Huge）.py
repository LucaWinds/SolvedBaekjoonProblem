from random import randrange
import sys
from math import gcd, sqrt
from collections import Counter

input = sys.stdin.readline


def pow(a, e, m):
    ret = 1
    t = a % m
    while e > 0:
        if e & 1:
            ret = ret * t % m
        t = t * t % m
        e >>= 1
    return ret

def miller_rabin(n, a):
    d = n - 1
    while d % 2 == 0:
        if pow(a, d, n) == n - 1:
            return True
        d //= 2
    t = pow(a, d, n)
    return t == n - 1 or t == 1

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False

    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n == a:
            return True
        if not miller_rabin(n, a):
            return False
    return True

def pollard_rho(n):
    if is_prime(n):
        return n

    if n == 1:
        return 1
    if n % 2 == 0:
        return 2

    x = randrange(2, n)
    y = x
    c = randrange(1, n)
    d = 1

    while d == 1:
        x = ((x ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        d = gcd(abs(x - y), n)

        if d == n:
            return pollard_rho(n)
    if is_prime(d):
        return d
    return pollard_rho(d)

def four_square(n):
    while n % 4 == 0:
        n //= 4
    return n % 8 == 7

def three_square(n):
    l = []
    while n > 1:
        d = pollard_rho(n)
        l.append(d)
        n //= d
    c = list(Counter(l).items())
    for i, n in c:
        if i % 4 == 3 and n % 2 == 1:
            return True
    return False

def solve(n):
    if four_square(n):
        return 4
    elif three_square(n):
        return 3
    elif int(sqrt(n)) ** 2 != n:
        return 2
    else:
        return 1


print(solve(int(input())))