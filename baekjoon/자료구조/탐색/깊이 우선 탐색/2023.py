# 신기한 소수 찾기

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())

# 소수 확인 함수
def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
3
def DSF(n):
    if len(str(n)) == N:
        print(n)
    else:
        for i in range(1, 10):
            if i % 2 == 0: # 짝수는 탐색 x
                continue
            if isPrime(n * 10 + i):
                DSF(n * 10 + i)

DSF(2)
DSF(3)
DSF(5)
DSF(7)