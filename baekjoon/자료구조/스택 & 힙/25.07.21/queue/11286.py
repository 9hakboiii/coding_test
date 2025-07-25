# 절댓값 힙 구현하기
# 절대값이 같을 땐, 음수를 우선 출력

from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline
N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1])) + '\n')
    else:
        # 절대값을 기준으로 정렬하고 같으면 음수 우선 정렬
        myQueue.put((abs(request), request))