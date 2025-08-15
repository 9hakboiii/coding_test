
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    ans = (a * b) // gcd(a, b)
    print(ans)
