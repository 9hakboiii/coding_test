# E: 지구 S: 태양 M 달

def extended_gcd(a, b):
    if b == 0:
        return (1, 0, a)
    x1, y1, g = extended_gcd(b, a % b)
    return (y1, x1 - (a // b) * y1, g)

def mod_inverse(a, m):
    x, y, g = extended_gcd(a, m)
    return x % m

def solve():
    E, S, M = map(int, input().split())
    E0, S0, M0 = (E % 15), (S % 28), (M % 19)

    m1, m2 = 15, 28
    inv15 = mod_inverse(m1, m2)
    k = ((S0 - E0) * inv15) % m2
    x12 = E0 + m1 * k
    M12 = m1 * m2

    m3 = 19
    inv420 = mod_inverse(M12 % m3, m3)
    t = ((M0 - x12 % m3) * inv420) % m3
    answer = x12 + M12 * t

    print(answer if answer != 0 else M12 * m3)

if __name__ == "__main__":
    solve()