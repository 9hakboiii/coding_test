# 알고리즘 수업 - 너비 우선 탐색 2
from collections import deque
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split()) # 정점 수, 간선 수, 시작 정점
A = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

# 내림 차순 정렬
for neighbors in A:
    neighbors.sort(reverse=True)

visited = [False] * (N + 1)
order = [0] * (N + 1)
cnt = 1

def bfs(start):
    global cnt
    q = deque([start])
    visited[start] = True
    order[start] = cnt

    while q:
        cur = q.popleft()
        for nxt in A[cur]:
            if not visited[nxt]:
                cnt += 1
                visited[nxt] = True
                order[nxt] = cnt
                q.append(nxt)

bfs(R)
print('\n'.join(map(str, order[1:])))