import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

size = 1
while size < n:
    size <<= 1
tree = [0] * (2 * size)

# 리프 노드 채우기
for i in range(n):
    tree[size + i] = int(input())

for i in range(size - 1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]

for _ in range(m + k):
    op, x, y = map(int, input().split())

    if op == 1:
        idx = size + x - 1
        tree[idx] = y
        idx //= 2
        while idx:
            tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
            idx //= 2
    else:
        left = size + x - 1
        right = size + y - 1
        s = 0

        while left <= right:
            if left & 1:
                s += tree[left]
                left += 1
            if not (right & 1):
                s += tree[right]
                right -= 1
            left //= 2
            right //= 2

        print(s)