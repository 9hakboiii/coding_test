import sys, math

gcd, lcm = map(int, sys.stdin.readline().split())
n = lcm // gcd

for i in range(math.isqrt(n), 0, -1):
    if n % i == 0:
        j = n // i
        if math.gcd(i, j) == 1:
            a = i * gcd
            b = j * gcd
            print(a, b)
            break

