import sys
input = sys.stdin.readline

def max_cuts(k_len, target):
    low, high = 1, max(k_len)
    ans = 0 

    while low <= high:
        mid = (low + high) // 2
        cnt = sum(length // mid for length in k_len)
        if cnt >= target:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans

k, n = map(int, input().split())
lens = [int(input()) for _ in range(k)]
print(max_cuts(lens, n))