import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
out_lines = []
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque((i, p) for i, p in enumerate(arr))
    counts = [0] * 10
    for p in arr:
        counts[p] += 1

    cur_max = 9
    while cur_max > 0 and counts[cur_max] == 0:
        cur_max -= 1

    printed = 0
    while q:
        idx, pri = q[0]
        if pri == cur_max:
            q.popleft()
            counts[pri] -= 1
            printed += 1
            if idx == m:
                out_lines.append(str(printed))
                break
            if counts[pri] == 0:
                while cur_max > 0 and counts[cur_max] == 0:
                    cur_max -= 1
        else:
            q.rotate(-1)

print("\n".join(out_lines))