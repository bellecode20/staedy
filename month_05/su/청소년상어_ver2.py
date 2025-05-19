import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

# 5:48 ~

from pprint import pprint
from copy import deepcopy

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def dfs(graph, fish_li, shark_pos, cur_answer):
    global answer

    # 2. 물고기 이동하기
    flag = True
    
    for fish_idx in range(1, 17):
        # print(f'{fish_idx} fish move')
        # pprint(graph)
        if fish_li[fish_idx] == -1:
            continue

        fish_r, fish_c = fish_li[fish_idx]
        # print("-------", fish_idx)
        # pprint(new_graph)
        # pprint(new_graph[fish_r][fish_c])
        fish_dir = graph[fish_r][fish_c][1]

        for i in range(8):
            next_fish_dir = (fish_dir + i) % 8
            fish_nr = fish_r + directions[next_fish_dir][0]
            fish_nc = fish_c + directions[next_fish_dir][1]
            graph[fish_r][fish_c][1] = next_fish_dir
            if fish_nr < 0 or fish_nc < 0 or fish_nr >= 4 or fish_nc >= 4:
                # print('영역밖')
                continue
            if graph[fish_nr][fish_nc] != -1 and graph[fish_nr][fish_nc][0] == -2:
                # print('상어')
                continue
            # 다음 위치의 값을 가져오기
            # 주의) 다음 위치가 -1이 아니라면 다음 위치의 값을 백업
            # swap 하기 
            # ㄱ. 다음 위치 -1이 아니라면 > fish_li / graph 둘 다 스왑
            # ㄴ. 다음 위치 -1이라면 > graph만 스왑

            if graph[fish_nr][fish_nc] != -1:
                n_idx, _ = graph[fish_nr][fish_nc]
                # print('if문')
                # swap 
                # print(graph[fish_nr][fish_nc], fish_nr, fish_nc)
                graph[fish_nr][fish_nc], graph[fish_r][fish_c] = graph[fish_r][fish_c], graph[fish_nr][fish_nc]
                fish_li[n_idx], fish_li[fish_idx] = fish_li[fish_idx], fish_li[n_idx]
                # print(graph[fish_nr][fish_nc])
            else:
                # print('else문')
                graph[fish_nr][fish_nc], graph[fish_r][fish_c] = graph[fish_r][fish_c], graph[fish_nr][fish_nc]
                fish_li[fish_idx] = [fish_nr, fish_nc]
            break

        flag = False
    if flag:  # 이동할 물고기가 없다 == 다 먹혔음
        answer = abs(answer, cur_answer)
        # print('분기 끝')
        return
    
    # print('물고기 이동 후')
    # pprint(graph)
    # dfs(graph, fish_li, shark_pos, cur_answer)
        
    # 1. 상어 이동
    # 지금 방향대로 탐색하기
    shark_dir = graph[shark_pos[0]][shark_pos[1]][1]
    
    # 다음 좌표 지정
    nr = shark_pos[0] + directions[shark_dir][0]
    nc = shark_pos[1] + directions[shark_dir][1]

    while 0 <= nr < 4 and 0 <= nc < 4:
        new_graph = deepcopy(graph)
        new_fish_li = deepcopy(fish_li)
        new_shark_pos = deepcopy(shark_pos)
        new_answer = cur_answer

        # 만약 빈 칸이면 continue
        if new_graph[nr][nc] == -1:
            nr += directions[shark_dir][0]
            nc += directions[shark_dir][1]
            continue

        # print()
        # print('먹기 전',new_answer)
        # pprint(new_graph)
        
        # 먹기
        dish_idx = new_graph[nr][nc][0]
        new_answer += dish_idx
        answer = max(answer, new_answer)


        new_graph[new_shark_pos[0]][new_shark_pos[1]] = -1  # 기존 위치 빈 칸으로.
        new_shark_pos = new_fish_li[dish_idx]  # 상어 이동. 좌표 업데이트
        new_graph[nr][nc] = [-2, new_graph[nr][nc][1]]  # 상어도 새로운 위치로 간다.
        new_fish_li[dish_idx] = -1  # 죽었음
        # print()
        # print('먹었음',new_answer)
        # pprint(new_graph)

        # 다음 좌표 탐색
        nr += directions[shark_dir][0]
        nc += directions[shark_dir][1]
        dfs(new_graph, new_fish_li, new_shark_pos, new_answer)
    # print('--------------------------------------------')
    # print('분기 끝')


N = 4
graph = [[[0, 0]] * N for _ in range(N)]  # 방향 기록
# graph = [[[0, 0]] * N for _ in range(N)]  # 방향 기록
fish_li = [[0, 0]] * 17
fish_li[0] = -1
answer = 0

shark_pos = [-1, -1]
row_i = 0

for i in range(N):
    # a1, b1, a2, b2, a3, b3, a
    line = list(map(int, input().split()))
    col_i = 0
    for j in range(0, N*2, 2):
        a, b = line[j], line[j+1]
        b -= 1  # 방향 인덱스 1부터 시작하므로 1만큼 빼준다.
        graph[i][col_i] = [a, b] # 생선 번호, 생선 방향
        fish_li[a] = [i, col_i]
        
        col_i += 1

# print("--초기값")
# pprint(graph)
# print(fish_li)

# 1. 상어 초기값 위치
dish_idx = graph[0][0][0]
answer += dish_idx
shark_pos = fish_li[dish_idx]
fish_li[dish_idx] = -1  # 빈칸은 -1
graph[0][0] = [-2, graph[0][0][1]]  # 상어는 -2

# print('graph------------------')
# pprint(graph)
dfs(graph, fish_li, shark_pos, answer)

print(answer)