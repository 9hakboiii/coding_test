import sys
input = sys.stdin.readline

n = int(input())
inf = 10**9
dp = [inf] * (n + 1)

dp[0] = 0
for i in range(1, n + 1):
    if i - 3 >= 0:
        dp[i] = min(dp[i], dp[i - 3] + 1)
    if i - 5 >= 0:
        dp[i] = min(dp[i], dp[i - 5] + 1)

print(dp[n] if dp[n] != inf else -1)