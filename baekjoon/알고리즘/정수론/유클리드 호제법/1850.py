from sys import stdin

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, stdin.readline().split())
g = gcd(a, b)
print('1' * g)