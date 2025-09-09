import sys
input = sys.stdin.readline

t = int(input())
ns = [int(input()) for _ in range(t)]
max_n = max(ns)

dp = [0] * (max_n + 1)
if max_n >= 1: dp[1] = 1
if max_n >= 2: dp[2] = 1
if max_n >= 3: dp[3] = 1

for i in range(4, max_n + 1):
    dp[i] = dp[i-2] + dp[i-3]

for n in ns:
    print(dp[n])
