import sys
input = sys.stdin.readline

n = int(input())
a = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = [0] * (n+1)

def DFS(v):
    visited[v] = True
    for i in a[v]:
        if not visited[i]:
            result[i] = i
            DFS(i)

for _ in range(n-1):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

DFS(1)
for i in range(2, n+1):
    print(result[i])