n = int(input())
dis = [[0] * n for _ in range(n)]

for i in range(n):
    dis[i] = list(map(int, input().split()))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dis[i][k] == 1 and dis[k][j] == 1:
                dis[i][j] = 1

for i in range(n):
    for j in range(n):
        print(dis[i][j], end=' ')
    print()