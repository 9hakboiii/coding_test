# 구간 합 구하기 2

n, c = map(int, input().split())
metrix_n = [[0] for _ in range(n)]
prefix_n = [[0] * (n+1) for _ in range(n)]
temp = 0

for i in range(n):
    metrix_n[i] = list(map(int, input().split()))

for i in range(n):
    temp = 0
    for j in range(1, n+1):
        temp += metrix_n[i][j-1]
        prefix_n[i][j] = temp

for _ in range(c):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0
    for row in range(x1-1, x2):
        result += prefix_n[row][y2] - prefix_n[row][y1-1]
    print(result)
