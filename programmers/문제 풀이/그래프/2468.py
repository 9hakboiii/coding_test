import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
area = [list(map(int, input().split())) for _ in  range(N)]
max_hegiht = max(max(row) for row in area)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, water_lever, visited):
    visited[x][y] = True
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and area[nx][ny] > water_lever:
                dfs(nx, ny, water_lever, visited)

ans = 0
for water in range(0, max_hegiht + 1):
    visited = [[False] * N for _ in range(N)]
    safe_cnt = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and area[i][j] > water:
                dfs(i, j, water, visited)
                safe_cnt += 1

    ans = max(ans, safe_cnt)
print(ans)