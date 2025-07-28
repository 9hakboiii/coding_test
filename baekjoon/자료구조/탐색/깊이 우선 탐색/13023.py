# 친구 관계 파악하기
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
arrive = False

def DSF(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True

    for i in A[now]:
        if not visited[i]:
            DSF(i, depth + 1)
        visited[i] = True

for i in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N):
    DSF(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)