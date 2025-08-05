# 삽입 정렬
# 번저 삽입 정렬 알고리즘으로 리스트를 오름차순으로 정렬하고
# 이후 필요한 시간의 합을 구한다.

N = int(input())
A = list(map(int, input().split()))
S = [0] * N

for i in range(1, N):
    insert_potin = 1
    insert_value = A[i]

    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_potin = j + 1
            break
        if j == 0:
            insert_potin = 0
        
    for j in range(i, insert_potin, -1):
        A[j] = A[j-1]
    
    A[insert_potin] = insert_value

S[0] = A[0]

for i in range(1, N):
    S[i] = S[i-1] + A[i]
sum = 0

for i in range(0, N):
    sum += S[i]

print(sum)


