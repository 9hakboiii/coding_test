# from collections import deque

# n = int(input())
# qe = deque()

# for i in range(1, n+1):
#     qe.append(i)

# while qe.__len__() > 1:
#     qe.popleft()
#     qe.append(qe.popleft())

# print(qe.pop())

n = int(input())
t = 0
while n>2**t:
    t += 1
print(int((n-2**(t-1))*2))