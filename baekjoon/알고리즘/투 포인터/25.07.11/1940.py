# 주몽의 명령

n, m = int(input()), int(input())
a = list(map(int, input().split()))
a.sort()
count = 0
i, j = 0, n - 1

while i < j:
    if a[i] + a[j] < m:
        i += 1
    elif a[i] + a[j] > m:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)