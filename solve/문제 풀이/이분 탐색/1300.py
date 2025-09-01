import sys
input = sys.stdin.readline

def count_leq(x: int, n:int) -> int:
    total = 0 
    for i in range(1, n+1):
        total += min(n, x // i)
    return total

def kth_num(n: int, k: int) -> int:
    left, right = 1, (n*n)
    ans = right

    while left <= right:
        mid = (left + right) // 2
        if count_leq(mid, n) >= k:
            ans = mid
            right = mid - 1
        elif count_leq(mid, n) <= k:
            left = mid + 1
    
    return ans

def main():
    n, k = int(input()), int(input())
    print(kth_num(n, k))

if __name__ == "__main__":
    main()