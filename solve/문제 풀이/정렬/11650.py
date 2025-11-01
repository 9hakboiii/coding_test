import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)] # 튜플 성질
points.sort()
sys.stdout.write('\n'.join(f'{x} {y}' for x, y in points))