import sys
input = sys.stdin.readline

def main():
    n = int(input())
    stair = [0] + [int(input()) for _ in range(n)]

    # 특수 케이스
    if n == 1:
        print(stair[1])
        return
    if n == 2:
        print(stair[1] + stair[2])
        return

    dp = [0] * (n + 1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    for i in range(3, n + 1):
        dp[i] = max(
            dp[i - 2] + stair[i],
            dp[i - 3] + stair[i - 1] + stair[i]
        )

    print(dp[n])

if __name__ == "__main__":
    main()