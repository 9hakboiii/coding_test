# n = int(input())
# A = [[] for _ in range(n)]
# visited = [False] * n
# d = [0] * n
# lcm = 1

# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

# def dfs(v):
#     visited[v] = True
#     for i in A[v]:
#         next = i[0]
#         if not visited[next]:
#             d[next] = d[v] * i[2] // i[1]
#             dfs(next)

# for i in range(n-1):
#     a, b, p, q = map(int, input().split())
#     A[a].append((b, p, q))
#     A[b].append((a, p, q))
#     lcm *= (p * q // gcd(p, q))

# d[0] = lcm
# dfs(0) # 임의의 노드에서 출발 
# mgcd = d[0]

# for i in range(1, n):
#     mgcd = gcd(mgcd, d[i])

# for i in range(n):
#     print(int(d[i] // mgcd), end=' ')


# BFS로 구현
import sys
from collections import deque
from fractions import Fraction
from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

def main():
    input = sys.stdin.readline
    n = int(input())
    adj = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        a, b, p, q = map(int, input().split())
        adj[a].append((b, p, q))
        adj[b].append((a, q, p))
    
    ratios = [None] * n
    ratios[0] = Fraction(1, 1)
    dq = deque([0])
    while dq:
        u = dq.popleft()
        for v, p, q in adj[u]:
            if ratios[v] is None:
                ratios[v] = ratios[u] * Fraction(q, p)
                dq.append(v)
    
    l_den = 1
    for frac in ratios:
        l_den = lcm(l_den, frac.denominator)

    values = [(frac * l_den).numerator for frac in ratios]
    g = values[0]
    for v in values[1:]:
        g = gcd(g, v)
    
    print(*[v // g for v in values])

if __name__ == "__main__":
    main()