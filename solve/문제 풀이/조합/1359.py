import math

def comb(n, r):
    if r > n or r < 0:
        return 0
    if r == 0 or r == n:
        return 1
    
    if r > n - r:
        r = n - r

    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n, m, k = map(int, input().split())
total = comb(n, m)
ans = 0.0
for i in range(k, m+1):
    if n-m < m-i:
        continue
    winning = comb(m, i) * comb(n-m, m-i)
    ans += winning / total

print(f'{ans:.9f}')