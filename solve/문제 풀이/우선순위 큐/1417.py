import sys
import heapq

input = sys.stdin.readline
n = int(input())
my_votes = int(input())
others = []
    
for _ in range(n - 1):
    votes = int(input())
    heapq.heappush(others, -votes)
    
bribes = 0
while others and my_votes <= -others[0]:
    top_votes = -heapq.heappop(others)
    top_votes -= 1
    my_votes += 1
    bribes += 1
    if top_votes > 0:
        heapq.heappush(others, -top_votes)
    
print(bribes)