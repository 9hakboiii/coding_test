import sys
input = sys.stdin.readline

def comb(n, k):
    if k < 0 or k > n:
        return 0
    if k > n - k:
        k = n - k
    
    res = 1
    for i in range(1, k+1):
        res = res * (n-i+1) // i
    return res

n = int(input())
print(comb(n, 4))