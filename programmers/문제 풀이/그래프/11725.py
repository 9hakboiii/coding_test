import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
a = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n-1):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

def dfs(v):
    for i in a[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i)

parent[1] = 1
dfs(1)

for i in range(2, n+1):
    print(parent[i])
    