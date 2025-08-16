import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

t = int(input())
data = []

for _ in range(t):
    parts = list(map(int, input().split()))
    _, nums = parts[0], parts[1:]
    data.append(nums)

for nums in data:
    total = 0
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            total += gcd(nums[i], nums[j])
    print(total)

"""
import math,itertools as t
for i in[*open(0)][1:]:print(sum(t.starmap(math.gcd,t.combinations(map(int,i.split()[1:]),2))))
"""