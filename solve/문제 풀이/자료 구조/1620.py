import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for i in range(1, n+1):
    name = input().rstrip()
    dic[name] = str(i)
    dic[str(i)] = name

ans = []
for _ in range(m):
    q = input().rstrip()
    ans.append(dic[q])
sys.stdout.write('\n'.join(ans))