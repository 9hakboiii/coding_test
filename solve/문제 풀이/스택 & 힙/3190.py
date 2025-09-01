# 뱀
import sys
from collections import deque
input = sys.stdin.readline

# 보드 크기, 사과 개수
n = int(input())
k = int(input())

# 사과 위치를 집합으로 관리
apples = set()
for _ in range(k):
    r, c = map(int, input().split())
    apples.add((r-1, c-1))

# 방향 전환 정보 입력
l = int(input())
turns = deque()
for _ in range(l):
    x, c = input().split()
    turns.append((int(x), c))

# 우, 하, 좌, 상 순서로 방향 벡터 정의
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
d = 0

snake = deque()
snake.append((0,0))
body = {(0,0)}

time = 0
x, y = 0, 0

while True:
    time += 1
    dx, dy = dirs[d]
    nx, ny = x + dx, y + dy

    # 벽 충돌 검사
    if not (0 <= nx < n and 0 <= ny < n):
        break

    # 자기 몸과 충돌 검사
    if (nx, ny) in body:
        break

    # 머리 이동
    snake.append((nx, ny))
    body.add((nx, ny))

    # 사과 먹었는지 여부 판단
    if (nx, ny) in apples:
        apples.remove((nx, ny)) 
    else:
        tx, ty = snake.popleft()
        body.remove((tx, ty))

    x, y = nx, ny

    # 시간에 맞춰 방향 전환
    if turns and turns[0][0] == time:
        _, c = turns.popleft()
        if c == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4

print(time)