from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    indegree[e] += 1

qe = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        qe.append(i)

while qe:
    now = qe.popleft()
    print(now, end=' ')
    for next in a[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            qe.append(next)
