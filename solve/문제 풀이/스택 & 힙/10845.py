# 큐
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
qe = deque()

for _ in range(n):
    ans = input().split()

    if ans[0] == 'push':
        qe.append(int(ans[1]))
    elif ans[0] == 'pop':
        print(qe.popleft() if qe else -1)
    elif ans[0] == 'size':
        print(len(qe))
    elif ans[0] == 'empty':
        print(0 if qe else 1)
    elif ans[0] == 'front':
        print(qe[0] if qe else -1)
    elif ans[0] == 'back':
        print(qe[-1] if qe else -1)