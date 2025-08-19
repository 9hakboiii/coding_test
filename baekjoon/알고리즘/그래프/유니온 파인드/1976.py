import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
        parent[rb] = ra

N = int(input())
M = int(input())

parent = list(range(N + 1))

for i in range(1, N+1):
    row = list(map(int, input().split()))
    for j in range(1, N+1):
        if row[j-1] == 1:
            union(i, j)

plan = list(map(int, input().split()))
root = find(plan[0])
for city in plan[1:]:
    if find(city) != root:
        print("NO")
        break
else:
    print("YES")