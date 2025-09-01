

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())
gdc, lcm = gcd(a, b), int(a * b / gcd(a, b))
print(gdc)
print(lcm)