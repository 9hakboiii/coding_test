import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = list(range(n + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx != ry:
        parent[ry] = rx

def checkSame(x, y):
    return find(x) == find(y)

for _ in range(m):
    q, a, b = map(int, input().split())
    if q == 0:
        union(a, b)
    else:
        print('YES\n' if checkSame(a, b) else 'NO\n')
        