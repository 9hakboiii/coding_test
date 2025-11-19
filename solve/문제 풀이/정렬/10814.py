import sys
input = sys.stdin.readline

n = int(input())
buckets = [[] for _ in range(201)]

for _ in range(n):
    age, name = input().split()
    buckets[int(age)].append(name)

ans = []
for age in range(1, 201):
    for name in buckets[age]:
        ans.append(f'{age} {name}')

sys.stdout.write('\n'.join(ans))