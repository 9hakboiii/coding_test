# print('SK' if int(input()) % 2 == 1 else 'CY')

# dp
n = int(input())
dp = [False] * (n+1)

if n >= 1:
    dp[1] = True
elif n >= 2:
    dp[2] = False
elif n >= 3:
    dp[3] = True

for i in range(4, n+2):
    dp[i] = not dp[i-1] or not dp[i-3]

print('SK' if dp[n] else 'CY')
