# 제곱 ㄴㄴ수
import math
mi, mx = map(int, input().split())
check = [False] * (mx - mi + 1)

for i in range(2, int(math.sqrt(mx)+1)):
    p = i * i
    st = int(mi / p)
    if mi % p != 0:
        st += 1
    
    for j in range(st, int(mx / p) + 1):
        check[int((j * p) - mi)] = True

cnt = 0
for i in range(0, mx - mi + 1):
    if not check[i]:
        cnt += 1

print(cnt)