import sys
input = sys.stdin.readline

r, c, w = map(int, input().split())
max = r + w
dp = [[0 for _ in range(max+1)] for _ in range(max+1)]

for i in range(1, max + 1):
    dp[i][1] = 1
    dp[i][i] = 1
    for j in range(2, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

ans = 0
for i in range(r, r+w):
    for j in range(c, c+(i-r+1)):
        ans += dp[i][j]

print(ans)