import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x, y, orient):
    visited[x][y] = True
    if orient == '-':
        for ny in (y - 1, y + 1):
            if 0 <= ny < M and not visited[x][ny] and board[x][ny] == '-':
                dfs(x, ny, orient)
    else:
        for nx in (x - 1, x + 1):
            if 0 <= nx < N and not visited[nx][y] and board[nx][y] == '|':
                dfs(nx, y, orient)

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            count += 1
            dfs(i, j, board[i][j])

print(count)