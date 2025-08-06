# 소수&팰린드롬
import math

N = int(input())
MAX = 10000001

is_prime = [True] * MAX
is_prime[0] = is_prime[1] = False

for i in range(2, int(math.sqrt(MAX)) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX, i):
            is_prime[j] = False

for i in range(N, MAX):
    if is_prime[i] and str(i) == str(i)[::-1]:
        print(i)
        break
