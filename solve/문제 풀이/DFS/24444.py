from collections import deque
import sys
input = sys.stdin.readline

def bfs(arr, start, n):
    visited = [0] * (n + 1)
    cnt = 1
    qe = deque([start])
    visited[start] = cnt

    while qe:
        node = qe.popleft()
        for nxt in arr[node]:
            if visited[nxt] == 0:
                cnt += 1
                visited[nxt] = cnt
                qe.append(nxt)

    return visited

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for adj in graph:
    adj.sort()

ans = bfs(graph, r, n)
for i in range(1, n + 1):
    print(ans[i])