# 연결 요소의 개수 구하기

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 노드, m: 엣지
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DSF(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DSF(i)
    
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DSF(i)

print(count)


