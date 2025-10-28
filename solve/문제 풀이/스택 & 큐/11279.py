from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
pq = PriorityQueue()

for _ in range(n):
    x = int(input())
    if x == 0:
        if pq.empty():
            print(0)
        else:
            print(abs(pq.get()))
    else:
        pq.put(-x)