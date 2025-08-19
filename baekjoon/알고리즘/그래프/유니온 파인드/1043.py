import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tmp = list(map(int, input().split()))
T = tmp[0]
truth_people = tmp[1:] if T > 0 else []
parent = list(range(N + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
        parent[rb] = ra

parties = []
for _ in range(M):
    data = list(map(int, input().split()))
    k = data[0]
    attendees = data[1:]
    parties.append(attendees)

    for i in range(1, k):
        union(attendees[0], attendees[i])

truth_roots = set(find(p) for p in truth_people)
count = 0
for attendees in parties:
    root0 = find(attendees[0])
    if root0 not in truth_roots:
        count += 1
        
print(count)