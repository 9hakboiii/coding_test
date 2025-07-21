# 구간합 공식
# s[i] = s[i-1] + a[i]
# i ~ j 까지의 구간 합: s[j] - s[i-1]

n, c = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp += i
    prefix_sum.append(temp)

for i in range(c):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])