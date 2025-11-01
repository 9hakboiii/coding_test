import sys
input = sys.stdin.readline

n = int(input().strip())
points = [tuple(map(int, input().split())) for _ in range(n)] # 튜플 성질
points.sort()

out = []
for x, y in points:
    out.append(f'{x} {y}')
sys.stdout.write('\n'.join(out))