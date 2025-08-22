from queue import PriorityQueue
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
dis = [sys.maxsize] * (V + 1)
visited = [False] * (V + 1)
myList = [[] for _ in range(V + 1)]
qe = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    myList[u].append((v, w))

qe.put((0, K))
dis[K] = 0

while qe.qsize() > 0:
    now = qe.get()
    c_v = now[1]
    if visited[c_v]:
        continue
    visited[c_v] = True

    for tmp in myList[c_v]:
        next = tmp[0]
        value = tmp[1]
        if dis[next] > dis[c_v] + value:
            dis[next] = dis[c_v] + value
            qe.put((dis[next], next))

for i in range(1, V+1):

    if visited[i]:
        print(dis[i])
    else:
        print("INF")