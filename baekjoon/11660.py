import sys
input = sys.stdin.readline
n, m = map(int, input().split())  # 2차원 배열 크기, 질의 개수
a_list= [list(map(int, input().split())) for _ in range(n)]
sum_list = [[0] * (n + 1) for _ in range(n)]


for i in range(n):  # 0~n
    temp = i
    sum_list[i][0] = i # i층 0호에 
    for j in range(n):
        temp = temp + a_list[i][j]
        sum_list[i][j+1] = temp

