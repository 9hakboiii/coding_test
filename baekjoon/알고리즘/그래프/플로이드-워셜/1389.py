import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dis = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    dis[i][i] = 0

for i in range(M):
    s, e = map(int, input().split())
    dis[s][e] = 1
    dis[e][s] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dis[i][j] > dis[i][k] + dis[k][j]:
                dis[i][j] = dis[i][k] + dis[k][j]

min = sys.maxsize
ans = -1

for i in range(1, N+1):
    temp = 0
    for j in range(1, N+1):
        temp +=  dis[i][j]
    if min > temp:
        min = temp
        ans = i

print(ans)