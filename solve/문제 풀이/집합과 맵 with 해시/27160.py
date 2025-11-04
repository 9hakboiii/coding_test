import sys
input = sys.stdin.readline

fruits = {
    'STRAWBERRY': 0,
    'BANANA': 0,
    'LIME': 0,
    'PLUM': 0
}

n = int(input())
for _ in range(n):
    fruit, num = input().split()
    if fruit in fruits:
        fruits[fruit] += int(num)

print('YES' if 5 in fruits.values() else 'NO')
