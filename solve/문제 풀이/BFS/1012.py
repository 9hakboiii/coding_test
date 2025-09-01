# 유기농 배추
from collections import deque
import sys
input = sys.stdin.readline

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    worms = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] and not visited[i][j]:
                worms += 1

                q = deque([(j, i)])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            if field[ny][nx] and not visited[ny][nx]:
                                visited[ny][nx] = True
                                q.append((nx, ny))
    print(worms)