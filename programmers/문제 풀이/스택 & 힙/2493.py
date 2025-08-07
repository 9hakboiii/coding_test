# 탑
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    heights = list(map(int, input().split()))
    stack = []
    ans = [0] * n

    for i, h in enumerate(heights):
        while stack and stack[-1][0] < h:
            stack.pop()

        if stack:
            ans[i] = stack[-1][1] + 1
        else:
            ans[i] = 0
        stack.append((h, i))

    print(*ans)

if __name__ == "__main__":
    main()