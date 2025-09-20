import sys

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))
    best = 0

    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                s = cards[i] + cards[j] + cards[k]
                if s <= M and s > best:
                    best = s
                    if best == M:
                        print(M)
                        return
    print(best)

if __name__ == "__main__":
    solve()