from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(n)]

dist = [[0] * m for _ in range(n)]
dist[0][0] = 1

qe = deque([(0, 0)])
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while qe:
    x, y = qe.popleft()
        
    if x == n-1 and y == m-1:
        print(dist[x][y])
        break
        
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
            
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and dist[nx][ny] == 0:
            dist[nx][ny] = dist[x][y] + 1
            qe.append((nx, ny))
