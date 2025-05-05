# https://www.acmicpc.net/problem/19236
# 풀이 진행 중...

import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 

from pprint import pprint
from collections import defaultdict
from collections import deque
from copy import deepcopy

directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

N = 4
graph = [[0, 0] * N for _ in range(N)]  # 방향 기록
pos_info = defaultdict(list)

row_i = 0

for i in range(N):
    # a1, b1, a2, b2, a3, b3, a
    line = list(map(int, input().split()))
    col_i = 0
    for j in range(0, N*2, 2):
        a, b = line[j], line[j+1]
        b -= 1  # 방향 인덱스 1부터 시작하므로 1만큼 빼준다.

        graph[row_i][col_i] = [a, b] # 생선 번호, 생선 방향
        pos_info[a] = [row_i, col_i]  # key는 생선 번호로 한다. 그래서 키가 있는지 여부를 조회하면 물고기 있는지 확인할 수 있음
        
        col_i += 1
    row_i += 1
        
pprint(graph)
pprint(pos_info)

SHARK = 100

queue = deque()
dead_fish = [graph[0][0][0]]  # 
print(dead_fish)

shark_dir = graph[0][0][1]  # 시작점에 위치한 생선 방향
graph[0][0] = [SHARK, shark_dir]  # 상어 인덱스, 상어 방향
queue.append(((0, 0), graph, pos_info, dead_fish))  # (상어 row, 상어 col), 그래프, 물고기 좌표 번호, 먹은 물고기 리스트

while queue:
    (row, col), cur_graph, cur_pos_info, d_fish = queue.popleft()  # 상어 row, 상어 col

    # 현재 방향대로 모두 탐색
    for _ in range(3):
        new_graph, new_pos_info = deepcopy(cur_graph), deepcopy(cur_pos_info)

        _, shark_dir = new_graph[row][col]
        next_row, next_col = row + directions[shark_dir][0], col + directions[shark_dir][1]
        # print("------------------------")
        # print(next_row, next_col)
        
        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
            break

        fish_i, fish_dir = new_graph[next_row][next_col]

        if fish_i == 0:  # 빈 칸인 경우
            continue

        # 1. 상어 움직이기
        new_graph[row][col] = [0, 0]  # 기존 상어 위치 빈칸으로 초기화
        new_graph[next_row][next_col] = [SHARK, fish_dir]  # 상어 움직이기
        del new_pos_info[fish_i]  # 생선 먹기
        d_fish.append(fish_i)

        row, col = next_row, next_col

        # 2. 생선 움직이기
        for f_i, f_pos in new_pos_info.items():
            print(new_graph)
            f_row, f_col = f_pos
            f_dir = new_graph[f_row][f_col][1]

            next_row, next_col = f_row + directions[f_dir][0], f_col + directions[f_dir][1]
            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                if new_graph[next_row][next_col] == 0 or new_graph[next_row][next_col] == SHARK:

                    # 방향 바꾸기
                    for i in range(len(directions)):
                        next_row, next_col = f_row + directions[f_dir][0], f_col + directions[f_dir][1]

                        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                            continue
                        if new_graph[next_row][next_col][0] == SHARK:
                            continue
                        
                        # if new_graph[next_row][next_col][0] != 
                        next_fish_i = new_graph[next_row][next_col][0]
                        if next_fish_i != 0:  # 다른 물고기
                            # 서로 위치 바꾸기
                            new_graph[f_row][f_col], new_graph[next_row][next_col] = new_graph[next_row][next_col], new_graph[f_row][f_col]  # swap
                            new_pos_info[fish_i], new_pos_info[next_fish_i]  = new_pos_info[next_fish_i], new_pos_info[fish_i]  # swap
                            break
                        
                        if next_fish_i == 0:  # 빈 칸인 경우
                            new_graph[f_row][f_col], new_graph[next_row][next_col] = new_graph[next_row][next_col], new_graph[f_row][f_col]  # swap  
                            new_pos_info[fish_i] = (next_row, next_col)
                            break
            
            queue.append(((next_row, next_col), new_graph, new_pos_info, d_fish))
                    
