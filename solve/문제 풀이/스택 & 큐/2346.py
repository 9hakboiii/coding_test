import sys
input = sys.stdin.readline

n = int(input())
moves = list(map(int, input().split()))
balloons = [(i + 1, moves[i]) for i in range(n)] # (번호, 이동값)

result = []
idx = 0  # 시작 인덱스

while balloons:
    num, k = balloons.pop(idx)
    result.append(str(num))

    if not balloons:
        break

    L = len(balloons)
    if k > 0:
        idx = (idx + (k - 1)) % L
    else:
        idx = (idx + k) % L

sys.stdout.write(' '.join(result))