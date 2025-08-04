# 수 정렬하기 2
import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_short(s, e):

    if e - s < 1: return
    mid = int(s + (e - s) / 2)
    merge_short(s, mid)
    merge_short(mid + 1, e)

    for i in range(s, e+1):
        tmp[i] += A[i]
    
    k = s
    index1 = s
    index2 = mid + 1

    while index1 <= mid and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
        
    while index1 <= mid:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1


N = int(input())
A = [0] * (N+1)
tmp = [0] * (N+1)

for i in range(1, N+1):
    A[i] = int(input())

merge_short(1, N)

for i in range(1, N+1):
    print(str(A[i]) + '\n')
