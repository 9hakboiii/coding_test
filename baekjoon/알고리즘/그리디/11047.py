# 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [0] * N
count = 0

for i in range(N):
    A[i] = int(input())

for i in range(N-1, -1, -1):
    if K >= A[i]:
        count += K // A[i]
        K = K % A[i]
    
print(count)
