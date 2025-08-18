import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rev = [[] for _ in range(n+1)]
for _ in range(m):
    A, B = map(int, input().split())
    rev[B].append(A)

ans = [0]*(n+1)
visited = [0]*(n+1)
token = 1

for start in range(1, n+1):
    queue = [start]
    head = 0
    visited[start] = token
    cnt = 0

    while head < len(queue):
        node = queue[head]
        head += 1
        for nxt in rev[node]:
            if visited[nxt] != token:
                visited[nxt] = token
                queue.append(nxt)
                cnt += 1

    ans[start] = cnt
    token += 1

mx = max(ans)
print(*[i for i in range(1, n+1) if ans[i] == mx])