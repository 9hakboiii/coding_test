import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a_list, sum_list = list(map(int, input().split())), []
sum_list = [0]
temp = 0

for i in a_list:
    temp = temp + i
    sum_list.append(temp)

answer = lambda i, j : sum_list[j] - sum_list[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(answer(i, j))
    