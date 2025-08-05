# 오큰수 구하기

import sys
n = int(input()) # 수열 길이
ans = [0] * n # 정답 리스트
A = list(map(int, input().split())) # 수열 
myStack = [] # 스택 리스트

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

for i in range(n):
    sys.stdout.write(str(ans[i]) + " ")