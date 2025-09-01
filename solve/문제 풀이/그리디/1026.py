# 연습
"""
def greedy_coin_change(amount, coins):
    coins.sort(reverse=True)
    
    count = 0
    used = []

    for coin in coins:
        num = amount // coin
        count += num
        amount -= coin * num
        used.append((coin, num))

    return count, used


coins = [10, 50, 100, 500]
amount = 760
total_count, breakdown = greedy_coin_change(amount, coins)

print(f'총 동전 갯수: {total_count}')
for coin, num in breakdown:
    if num > 0:
        print(f'{coin}원 동전: {num}개')
"""

# 보물
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
ans = sum(a * b for a, b in zip(A, B))
print(ans)