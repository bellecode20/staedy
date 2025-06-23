# [BOJ] 경사로 https://www.acmicpc.net/problem/14890

import os
import sys
from pprint import pprint


# 현재 파일이 있는 디렉토리를 기준으로 작업 디렉토리 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
sys.stdin = open('input.txt', "r")


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def check_road(line):
    idx = 0
    visited = [0] * N
    while idx < N:
        if idx == N-1:
            return True
        
        if line[idx + 1] == line[idx]:
            idx += 1
        elif line[idx + 1] == line[idx] -1: # 내리막 경사로. 대소비교가 아니라 1차이나야 한다.
            if idx + L >= N:  # 영역 밖
                return False
            for gap in range(1, L+1):  # 다음 칸부터가 경사로가 된다
                if visited[idx + gap] == 1 or line[idx + gap] != line[idx+1]:
                    return False
                visited[idx + gap] = 1
            idx += L
        elif line[idx + 1] == line[idx] + 1:  # 오르막 경사로. 대소비교가 아니라 1차이나야 한다
            if idx - (L - 1) < 0:  # 영역 밖
                return False
            
            for gap in range(L):  # 현재 위치부터가 경사로가 된다
                if visited[idx - gap] == 1 or line[idx - gap] != line[idx]:
                    return False
                visited[idx-gap] = 1
            idx += 1
        else:
            return False
    return True

for i in range(N):
    row_line = board[i]
    col_line = [board[j][i] for j in range(N)]
    
    if check_road(row_line):
        answer += 1
    if check_road(col_line):
        answer += 1

print(answer)