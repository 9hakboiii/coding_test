# k번쨰 수

N, K = int(input()), int(input())
start = 1
end = K
ans = 0

while start <= end:
    mid = int((start + end) / 2)
    cnt = 0

    for i in range(1, N + 1):
        cnt += min(int(mid / i), N)
    if cnt < K:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)
