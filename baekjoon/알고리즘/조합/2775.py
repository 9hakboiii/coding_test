import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    dp = list(range(n+1))

    for _ in range(k):
        for i in range(1, n+1):
            dp[i] += dp[i-1]
    print(dp[n])