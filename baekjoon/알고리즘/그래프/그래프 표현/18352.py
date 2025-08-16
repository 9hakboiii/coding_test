import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
A = [[] for _ in range(N + 1)]
answer = []
visited = [-1] * (N + 1)

def BFS(v):
    qe = deque()
    qe.append(v)
    visited[v] += 1
    
    while qe:
        node = qe.popleft()
        for i in A[node]:
            if visited[i] == -1:
                visited[i] = visited[node] + 1
                qe.append(i)

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
BFS(X)

for i in range(N+1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)