# 수 정렬하기2

import sys
print = sys.stdout.write
input = sys.stdin.readline

def merge_short(s, e):
    if e - s < 1: return # 재귀 무한루프 방지
    m = int(s + (e - s) / 2) # 오버플로우 방지
    merge_short(s, m) # 재귀 함수 호출로 병합할 범위를 분할 
    merge_short(m + 1, e)
    for i in range(s, e+1):
        tmp[i] = A[i]
    
    k = s
    index1 = s
    index2 = m + 1

    # index1, 2의 값 비교 후 정렬
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    
    # 한쪽 그룹이 모두 선택된 후 남아 있는 값 정리
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1
    

N = int(input())
A = [0] * int(N + 1)
tmp = [0] * int(N + 1)

# 수열 값 채우기
for i in range(1, N+1):
    A[i] = int(input())

# 병합 정렬
merge_short(1, N)

for i in range(1, N+1):
    print(str(A[i]) + '\n')