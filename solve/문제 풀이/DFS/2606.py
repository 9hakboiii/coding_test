# 바이러스
import sys
input = sys.stdin.readline

node, link = int(input()), int(input())
A = [[] for _ in range(node + 1)]
visited = [False] * (node + 1)
cnt = 0

def DFS(v):
    global cnt
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            cnt += 1
            DFS(i)

for _ in range(link):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

DFS(1)
print(cnt)

