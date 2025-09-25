import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    num = input().split()
    if num[0] == '1':
        stack.append(int(num[1]))
    elif num[0] == '2':
        print('-1' if not stack else stack.pop())
    elif num[0] == '3':
        print(str(len(stack)))
    elif num[0] == '4':
        print('1' if not stack else '0')
    else:
        print('-1' if not stack else stack[-1])