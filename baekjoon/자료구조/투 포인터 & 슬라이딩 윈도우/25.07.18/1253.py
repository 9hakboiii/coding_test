# 좋은 수 구하기 (골드 5)
import sys

input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
A.sort() # 정렬 (nlogn)
count = 0

for k in range(n):
    find = A[k]
    i = 0
    j = n - 1

    while i < j:
        if A[i] + A[j] == find:
            if i != k and j != k: # 자기 자신은 포함 X
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif  A[i] + A[j] < find:
            i += 1
        else: 
            j -= 1

print(count)
