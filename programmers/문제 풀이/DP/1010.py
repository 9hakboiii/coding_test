import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    # 서쪽, 동쪽
    prev = [0] * (M+1)
    curr = [0] * (M+1)

    for i in range(1, M+1):
        prev[i] = i

    for i in range(2, N+1):
        for j in range(i, M+1):
            if i == j:
                curr[j] = 1
            else:
                curr[j] = prev[j-1] + curr[j-1]

        prev, curr = curr, [0] * (M+1)
        
    print(prev[M])
