from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
qe = deque()
for _ in range(n):
    st = input().split()
    cmd = st[0]

    if cmd == 'push':
        qe.append(int(st[1]))
    elif cmd == 'pop':
        if qe:
            print(qe.popleft())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(qe))
    elif cmd == 'empty':
        print(1 if not qe else 0)
    elif cmd == 'front':
        if qe:
            print(qe[0])
        else:
            print(-1)
    elif cmd == 'back':
        if qe:
            print(qe[-1])
        else:
            print(-1)