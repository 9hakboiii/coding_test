import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

n_arr.sort()

res = []
for target in m_arr:
    left = bisect_left(n_arr, target)
    right = bisect_right(n_arr, target)
    res.append(str(right - left))

print(' '.join(res))