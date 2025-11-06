import sys
input = sys.stdin.readline

def sol(s):
    cnt = 0
    for ch in s:
        if ch == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return 'NO'
    return 'YES' if cnt == 0 else 'NO'

n = int(input())

for _ in range(n):
    st = input().strip()
    sys.stdout.write(sol(st) + '\n')