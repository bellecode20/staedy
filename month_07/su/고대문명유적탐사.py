# [삼성 기출 - 2024 상반기 오전 1번 문제] https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ancient-ruin-exploration/description

import os
import sys
# 현재 파일이 있는 디렉토리를 기준으로 작업 디렉토리 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
sys.stdin = open('input.txt', "r")

from copy import deepcopy
import pprint
from collections import deque

# 특정 영역만 회전시키는 법
# 누적 회전. 회전 시 계속 원본 보드판 참조해서 회전이 90 180 270 안되고 90도만 반복해서 회전하고 있었음
# 함수 파라미터로 보드판 전달받았으면 함수 내에서 그 보드판 수정하면 실제 그 변수 값 바뀌기 때문에 굳이 새 보드판을 리턴하지 않아도 된다.

N = 5
K, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
pieces = list(map(int, input().split()))
queue = deque(pieces)
def all_print(param):
    print("격자판")
    for i in range(len(param)):
        print(param[i])

def get_rotated_board(cur_board, sr, sc):
    new_board = deepcopy(cur_board)
    for i in range(3):
        for j in range(3):
            real_sr, real_sc = sr + i, sc + j

            new_rel_r = j
            new_rel_c = 2 - i

            new_abs_sr = sr + new_rel_r
            new_abs_sc = sc + new_rel_c

            new_board[new_abs_sr][new_abs_sc] = cur_board[real_sr][real_sc]  # 주의

    return new_board

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def explore(rotated_board):
    # [1] 1차 획득 계산 & 보드판 선택
    cells_to_be_removed = []
    visited = [[0] * N for _ in range(N)]
    score = 0

    def dfs(r, c, goal, collected_coords):
        visited[r][c] = 1
        collected_coords.append((c, r*-1))  # 후에 정렬하기 위해 이렇게 넣는다.
        cnt = 1
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if rotated_board[nr][nc] != goal or visited[nr][nc] == 1:
                continue

            cnt += dfs(nr, nc, goal, collected_coords)

        return cnt

    for i in range(N):
        for j in range(N):
            visited_cells = []   # 
            if visited[i][j] == 1:
                continue
            
            cnt = dfs(i, j, rotated_board[i][j], visited_cells)
            if cnt >= 3:
                score += cnt  # 
                cells_to_be_removed.extend(visited_cells)
    
    return score, cells_to_be_removed

def fill_board(cells, current_board):
    # [2] 유물 채우기 
    global queue
    for cell_col, cell_row in cells:
        new_piece = queue.popleft()
        cell_row = abs(cell_row)  # 양수로 변환하기
        current_board[cell_row][cell_col] = new_piece
    

for k in range(K):
    # 탐사 진행 (격자 선택)
    total_score = 0
    candidates = []
    for start_r in range(0, 3):
        for start_c in range(0, 3):
            rotated = deepcopy(board)
            for angle in range(3):  # 90, 180, 270
                rotated = get_rotated_board(rotated, start_r, start_c)  # 격자판 회전
                copied_board = deepcopy(rotated)
                score, cells_to_be_removed = explore(copied_board)
                if score > 0:
                    candidates.append((-score, angle, start_c + 1, start_r + 1, copied_board, cells_to_be_removed))  # 보드판 선택을 위함
    if not candidates:  # 탐사 그만두기
        break
    selected = sorted(candidates)[0] 
    selected_score, _, _, _, selected_board, selected_cells = selected
    total_score += abs(selected_score)

    fill_board(sorted(selected_cells), selected_board)
    
    # 연쇄 획득
    while True:
        re_score, re_cells_to_be_removed = explore(selected_board)  # 재탐색. 방문처리한다.
        if re_score <= 0:  # 탐사 그만두기
            break
        total_score += re_score
        fill_board(sorted(re_cells_to_be_removed), selected_board)

    board = selected_board  # 현재 보드판으로 참조점 변경
    print(total_score, end=" ")