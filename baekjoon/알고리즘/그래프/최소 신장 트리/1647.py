import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])

uf = UnionFind(n)
total = 0
max_edge = 0

for s, e, w in edges:
    if uf.union(s, e):
        total += w
        if w > max_edge:
            max_edge = w

print(total - max_edge)