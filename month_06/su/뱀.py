# [BOJ] 뱀 https://www.acmicpc.net/problem/3190

import os
import sys

# 현재 파일이 있는 디렉토리를 기준으로 작업 디렉토리 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
sys.stdin = open('input.txt', "r")

# 머리랑 꼬리를 계속 생신해가야한다.
# 특히 꼬리가 줄어든 경우 계속 꼬리 위치를 갱신해야 하는데 별도 변수로 관리하기보단 큐에 넣고 삽입/삭제하는 식으로 관리한다.
# 
from collections import deque
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
APPLE = 1
SNAKE = 2
board[0][0] = SNAKE
for k in range(K):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1

L = int(input())
queue = deque()
for l in range(L):
    X, C = input().split()
    queue.append((int(X), C))

time = 0
head = [0, 0, 1]  # row, col, 방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
snake_queue = deque()
snake_queue.append((0, 0)) # 머리(꼬리) 넣기

while True:
    if queue and queue[0][0] == time:
        X, C = queue.popleft()
        # 방향 전환
        if C == "L": 
            head[2] = (head[2] + 3) % 4
        else:
            head[2] = (head[2] + 1) % 4

    # 다음 칸 확장(머리)
    nr, nc = head[0] + dr[head[2]], head[1] + dc[head[2]]
    
    if nr < 0 or nc < 0 or nr >= N or nc >= N:
        time += 1
        break
    if board[nr][nc] == SNAKE:
        time += 1
        break

    snake_queue.append((nr, nc))  # 머리를 추가한다
    if board[nr][nc] == APPLE:
        board[nr][nc] = SNAKE
    else:
        board[nr][nc] = SNAKE
        tr, tc = snake_queue.popleft()  # 꼬리 삭제
        board[tr][tc] = 0

    head[0], head[1] = nr, nc
    time += 1

print(time)
