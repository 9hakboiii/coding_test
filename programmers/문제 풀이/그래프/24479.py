import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
a = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for nb in a:
    nb.sort()

order = [0] * (N+1)
cnt = 1

stack = [R]
while stack:
    v = stack.pop()
    if order[v]:
        continue
    order[v] = cnt
    cnt += 1
    
    for u in reversed(a[v]):
        if not order[u]:
            stack.append(u)

sys.stdout.write('\n'.join(map(str, order[1:])))