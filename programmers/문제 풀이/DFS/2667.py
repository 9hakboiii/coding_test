# 단지번호붙이기

import sys
input = sys.stdin.readline  

def DFS(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and map[nx][ny] == '1':
                DFS(nx, ny)

n = int(input().strip())
map = [input().strip() for _ in range(n)]
visited = [[False] * n for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

complex_cnt = []
for i in range(n):
    for j in range(n):
        if map[i][j] == '1' and not visited[i][j]:
            cnt = 0
            DFS(i, j)
            complex_cnt.append(cnt)

complex_cnt.sort()
print(len(complex_cnt))
for cnt in complex_cnt:
    print(cnt)