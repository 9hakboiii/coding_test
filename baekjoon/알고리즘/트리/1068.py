import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
visited = [False] * (n)
tree = [[] for _ in range(n)]
ans = 0
p = list(map(int, input().split()))

for i in range(n):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i

def DFS(v):
    global ans
    visited[v] = True
    cNode = 0
    for i in tree[v]:
        if not visited[i] and i != deletedNode:
            cNode += 1
            DFS(i)

    if cNode == 0:
        ans += 1

deletedNode = int(input())
if deletedNode == root:
    print(0)
else:
    DFS(root)
    print(ans)