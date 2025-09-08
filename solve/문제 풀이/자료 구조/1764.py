import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 듣, 보
dj = set(input().rstrip() for _ in range(n))

common = []
for _ in range(m):
    name = input().rstrip()
    if name in dj:
        common.append(name)
common.sort()
sys.stdout.write('\n'.join([str(len(common))] + common))