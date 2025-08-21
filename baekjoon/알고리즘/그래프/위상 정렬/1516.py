from collections import deque

n = int(input())
a = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
build = [0] * (n + 1)

for i in range(1, n+1):
    inputList = list(map(int, input().split()))
    build[i] = (inputList[0])
    index = 1
    while True:
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:
            break
        a[preTemp].append(i)
        indegree[i] += 1

qe = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        qe.append(i)

result = [0] * (n + 1)
while qe:
    now = qe.popleft()
    for next in a[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now] + build[now])
        if indegree[next] == 0:
            qe.append(next)

for i in range(1, n+1):
    print(result[i] + build[i])