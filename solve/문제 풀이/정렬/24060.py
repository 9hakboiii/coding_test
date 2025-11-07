import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def merge_sort(s, e):
    if s >= e: return

    mid = (s + e) // 2
    merge_sort(s, mid)
    merge_sort(mid + 1, e)
    merge(s, mid, e)

def merge(s, mid, e):
    global cnt, ans, arr, k
    tmp = []
    i, j = s, mid + 1

    while i <= mid and j <= e:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    if i <= mid:
        tmp.extend(arr[i:mid+1])
    if j <= e:
        tmp.extend(arr[j:e+1])

    for i, v in enumerate(tmp):
        arr[s + i] = v
        cnt += 1
        if cnt == k:
            ans = v

n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
ans = -1

merge_sort(0, n - 1)
print(ans)