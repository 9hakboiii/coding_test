# 수 정렬하기 1
# sort() 대신 버블 정렬 이용

N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

# O(n^2)
for i in range(N-1): # 0~4
    for j in range(N-1-i): # 0~4-i
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

for i in range(N):
    print(A[i])