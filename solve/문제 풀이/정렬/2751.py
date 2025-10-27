import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    ans = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1

    ans.extend(left[i:])
    ans.extend(right[j:])
    return ans

n = int(input())
arr = [int(input()) for _ in range(n)]
print('\n'.join(map(str, merge_sort(arr))))