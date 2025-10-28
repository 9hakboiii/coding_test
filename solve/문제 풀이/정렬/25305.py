import sys
input = sys.stdin.readline

n, k = map(int, input().split())
st = list(map(int, input().split()))
st.sort(reverse=True)
qe = []

for i in range(k):
    qe.append(st[i])
print(qe[-1])
