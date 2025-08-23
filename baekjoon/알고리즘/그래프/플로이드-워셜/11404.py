import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
d = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    d[i][i] = 0

for i in range(m):
    s, e, w = map(int, input().split())
    if d[s][e] > w:
        d[s][e] = w

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if d[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(d[i][j], end=' ')
    print()