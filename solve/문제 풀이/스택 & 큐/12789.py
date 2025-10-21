import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
target = 1

for x in arr:
    stack.append(x)
    while stack and stack[-1] == target:
        stack.pop()
        target += 1
print('Nice' if target == n+1 else 'Sad')


