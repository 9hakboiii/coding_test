# 버블 정렬 프로그램 1
# N의 최대 범위가 500,000
# sorted(): 이터러블 객체 모두 사용 가능, 새로운 리스트 반환(원본 유지)
import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i)) # 정렬 기준을 고려하여 데이터, index 순서로 저장

Max = 0
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] - i
    
print(Max + 1)



