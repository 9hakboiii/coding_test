# 1
# n = int(input())
# score = list(map(int, input().split()))
# top = max(score)
# num, avg = 0, 0

# for i in score:
#     num += i / top * 100

# avg = num / n
# print(avg)

# 2
n = int(input())
score = list(map(int, input().split()))
mymax = max(score)
sum = sum(score)

print(sum * 100 / mymax / n)