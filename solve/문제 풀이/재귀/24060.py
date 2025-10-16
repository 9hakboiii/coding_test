import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

def merge_sort(a, tmp, s, e):
    if e - s <= 1:
        return
    m = (s + e) // 2
    merge_sort(a, tmp, s, m)
    merge_sort(a, tmp, m, e)

    i, j, k = s, m, s
    while i < m and j < e:
        if a[i] <= a[j]:
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            j += 1
        _write(tmp[k])
        k += 1

    while i < m:
        tmp[k] = a[i]
        i += 1
        _write(tmp[k])
        k += 1

    while j < e:
        tmp[k] = a[j]
        j += 1
        _write(tmp[k])
        k += 1

    for t in range(s, e):
        a[t] = tmp[t]

def _write(val):
    global cnt, K
    cnt += 1
    if cnt == K:
        print(val)
        sys.exit(0)

n, K = map(int, input().split())
a = list(map(int, input().split()))
tmp = [0] * n
cnt = 0

merge_sort(a, tmp, 0, n)
print(-1)