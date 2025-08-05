# k번째 수 구하기
"""
pivot 선정 방법
1. pivot == k: k번째 수를 찾은 것이므로 알고리즘을 종료
2. pivot > k: pivot의 왼쪽 부분에 k가 있으므로 왼쪽(S ~ pivot-1)만 정렬을 수행
3. pivot < k: pivot의 오른쪽 부분에 k가 있으므로 오른쪽(pivot+1 ~ S) 정렬을 수행
"""
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))


# 퀵 정렬 함수
def quickSort(start, end, k):
    global A # 전역함수
    if start < end:
        pivot = partition(start, end)
        if pivot == k:
            return
        elif k < pivot:
            quickSort(start, pivot-1, k)
        else:
            quickSort(pivot+1, end, k)

# pivot 구하기 함수
def swap(start, end):
    global A
    temp = A[start]
    A[start] = A[end]
    A[end] = temp

def partition(start, end):
    global A

    if start + 1 == end:
        if A[start] > A[end]:
            swap(start, end)
        return end

    M = (start + end) // 2
    swap(start, M)
    pivot = A[start]
    i = start + 1
    j = end

    while i <= j:
        while pivot < A[j] and j > 0:
            j = j - 1
        while pivot > A[i] and i < len(A) - 1:
            i = i + 1
        if i <= j:
            swap(i, j)
            i = i + 1
            j = j - 1
    
    A[start] = A[j]
    A[j] = pivot
    return j

quickSort(0, N-1, K-1)
print(A[K-1])

