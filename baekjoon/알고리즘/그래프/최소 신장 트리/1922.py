# from queue import PriorityQueue
# import sys
# input = sys.stdin.readline

# n, m = int(input()), int(input()) # 노드, 간선
# pq = PriorityQueue()
# network = [0] * (n+1)

# def find(n):
#     if n == network[n]:
#         return n
#     else:
#         network[n] = find(network[n])
#         return network[n]
    
# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a != b:
#         network[a] = b

# for i in range(n+1):
#     network[i] = i

# for _ in range(m):
#     s, e, w = map(int, input().split())
#     pq.put((w, s, e))

# result = 0
# cnt = 0

# while cnt < n - 1:
#     w, s, e = pq.get()
#     if find(s) != find(e):
#         union(s, e)
#         result += w
#         cnt += 1

# print(result)

# 2
import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        parent[b] = a
        return True
    return False

n, m = int(input()), int(input())
edges = []
for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append((w, s, e))

edges.sort()
parent = [i for i in range(n+1)]
total_cost = 0
cnt = 0

for w, s, e in edges:
    if union(parent, s, e):
        total_cost += w
        cnt += 1
        if cnt == n-1:
            break

print(total_cost)
