import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(u):
    global cnt
    visited[u] = cnt

    for v in graph[u]:
        if visited[v] == 0:
            cnt += 1
            dfs(v)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort(reverse=True)

visited = [0] * (N+1)
cnt = 1

dfs(R)
for i in range(1, N+1):
    print(visited[i])