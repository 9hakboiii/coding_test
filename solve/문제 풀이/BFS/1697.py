from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

MAX = 100000
visited = [-1] * (MAX + 1)

def bfs(start):
    q = deque([start])
    visited[start] = 0

    while q:
        x = q.popleft()
        if x == k:
            return visited[k]
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)

    return visited[k]

print(bfs(n))