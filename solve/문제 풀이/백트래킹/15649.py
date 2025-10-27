import sys

def backtracking(n, m, visited, path):
    if len(path) == m:
        sys.stdout.write(' '.join(map(str, path)) + '\n')
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            backtracking(n, m, visited, path)
            path.pop()

            visited[i] = False

n, m = map(int, sys.stdin.readline().split())
visited = [False] * (n + 1)
backtracking(n, m, visited, [])
