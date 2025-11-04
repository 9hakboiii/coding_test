import sys
input = sys.stdin.readline

n = int(input())
lev = {}

for _ in range(n):
    name, action = input().split()
    lev[name] = action

sys.stdout.write('\n'.join(sorted([name for name in lev if lev[name] == 'enter'], reverse=True)))