import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[x][y]:
        return False
    if board[x][y] == -1:
        print("HaruHaru")
        sys.exit(0)
    visited[x][y] = True
    step = board[x][y]
    dfs(x + step, y)
    dfs(x, y + step)
    return False

n = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dfs(0, 0)
print("Hing")