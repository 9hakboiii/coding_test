# 두 수의 합

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()
x = int(input())
count = 0
i, j = 0, n-1

while i < j:
    if num[i] + num[j] == x:
        count += 1
        i += 1
        j -= 1
    elif num[i] + num[j] > x:
        j -= 1
    elif num[i] + num[j] < x:
        i += 1

print(count)