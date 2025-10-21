import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
stack = deque()

for _ in range(k):
    n = int(input())
    if n == 0:
        stack.pop()
        continue
    stack.append(n)

print(sum(stack))
