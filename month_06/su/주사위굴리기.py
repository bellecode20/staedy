# [BOJ] 주사위 굴리기 https://www.acmicpc.net/problem/14499
import os
import sys
from pprint import pprint
# 현재 파일이 있는 디렉토리를 기준으로 작업 디렉토리 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
sys.stdin = open('input.txt', "r")

N, M, row, col, K = map(int, input().split())  
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

R, L, U, D = range(4)
NORTH, TOP, SOUTH, BOTTOM, WEST, EAST = range(6)
commands = list(map(int, input().split()))  

dice = [0, 0, 0, 0, 0, 0]


dr = [0, 0, -1, 1] # 오 왼 위 아
dc = [1, -1, 0, 0]

for cmd in commands:
    cmd -= 1
    nr = row + dr[cmd]
    nc = col + dc[cmd]
    if nr < 0 or nc < 0 or nr >= N or nc >= M:
        continue
    # print("nr, nc", nr, nc)
    
    temp = dice[:]
    if cmd == L:  
        temp[TOP] = dice[EAST]
        temp[EAST] = dice[BOTTOM]
        temp[BOTTOM] = dice[WEST]
        temp[WEST] = dice[TOP]
        if board[nr][nc] == 0:
            board[nr][nc] = temp[BOTTOM]
        else:
            temp[BOTTOM] = board[nr][nc]
            board[nr][nc] = 0
    elif cmd == R:
        temp[WEST] = dice[BOTTOM]
        temp[BOTTOM] = dice[EAST]
        temp[EAST] = dice[TOP]
        temp[TOP] = dice[WEST]
        if board[nr][nc] == 0:
            board[nr][nc] = temp[BOTTOM]
        else:
            temp[BOTTOM] = board[nr][nc]
            board[nr][nc] = 0
    elif cmd == D:
        temp[TOP] = dice[NORTH]
        temp[NORTH] = dice[BOTTOM]
        temp[BOTTOM] = dice[SOUTH]
        temp[SOUTH] = dice[TOP]
        if board[nr][nc] == 0:
            board[nr][nc] = temp[BOTTOM]
        else:
            temp[BOTTOM] = board[nr][nc]
            board[nr][nc] = 0
    else:
        temp[TOP] = dice[SOUTH]
        temp[SOUTH] = dice[BOTTOM]
        temp[BOTTOM] = dice[NORTH]
        temp[NORTH] = dice[TOP]
        if board[nr][nc] == 0:
            board[nr][nc] = temp[BOTTOM]
        else:
            temp[BOTTOM] = board[nr][nc]
            board[nr][nc] = 0
    dice = temp
    row, col = nr, nc
    print(dice[TOP])