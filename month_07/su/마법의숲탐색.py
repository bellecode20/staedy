# [삼성 기출 - 기출 문제 / 2024 상반기 오후 1번 문제] https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/magical-forest-exploration/description

import os
import sys
# 현재 파일이 있는 디렉토리를 기준으로 작업 디렉토리 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
sys.stdin = open('input.txt', "r")
from copy import deepcopy
from pprint import pprint
from collections import deque

R, C, K = map(int, input().split())
board = [[-2] * C for _ in range(3)] + [[0] * C for _ in range(R)]

pprint(board)
# 보드판을 행 기준으로 +3 크기로 만들기 (처음에 골렘 위치 가늠하기 위해서)


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

golem = [(-1, 0), (0, 0), (0, 1), (1, 0), (0, -1)]  # 센터를 기준으로 십자 모양 좌표

# EMPTY = 0
EXIT = -1

for k in range(1, K + 1):
    center_col, d = map(int, input().split())  # 골렘의 중앙 칸, 출구 방향
    center_col -= 1  # 문제는 1부터 시작하므로 1은 뺀다.
    center_row = 1  # 십자 모양이니깐..
    
    # 맨 위칸에 넣기
    for dr, dc in golem:
        nr, nc = center_row + dr, center_col + dc
        board[nr][nc] = k
    pprint(board)
    break
    # 아래 세 개만 계속 고려할지? 아니면 그냥 골렘 전체 십자 모양을 고려할지? 
    
    # 처음 내려올 때
    # [1] 1칸
    # [2] 아래 세칸
    # [3] 아래 세칸

    # 그 외 케이스
    # 아래 세칸 * 3

    
    # 센터 기준으로 3x3 크기

    # 저장시 +1 해서 저장해야 한다.
    