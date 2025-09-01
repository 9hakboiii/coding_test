# 단어 순서 뒤집기
# N = int(input())
# A = [['']] * N
# stack = []

# for i in range(N):
#     A[i] = input().split()

# for i in range(N):
#     ans = ''

#     for j in range(len(A[i])):
#         stack.append(A[i][j])
    
#     for j in range(len(stack)):
#         ans += stack.pop() + ' '

#     print(f'Case #{i+1}: {ans}')

# 2
import sys

n = int(sys.stdin.readline())
stack = [sys.stdin.readline() for _ in range(n)]

for i in range(n):
    print(f'Case #{i+1}: '+' '.join(stack[i].split()[::-1]))