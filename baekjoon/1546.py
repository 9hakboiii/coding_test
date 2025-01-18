n = input()
score = list(map(int, input().split()))
high_score = max(score)
# (((a + b + c) * 100) / M) / n
sum_score = sum(score)
print(sum_score * 100 / high_score / int(n))
