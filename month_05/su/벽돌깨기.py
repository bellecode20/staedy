import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

# 5:48 ~

from pprint import pprint
from copy import deepcopy
from collections import defaultdict
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def attack():
    return 

def dfs(graph, cnt, depth, top_pos):
    global answer
    # if depth > N:  [fix] 종료조건 오류
    if depth == N:
        # answer = max(answer, cnt)
        return
    
    for c in range(W):
        if top_pos[c] == -1:  # 벽돌이 없는 경우
            continue

        # 벽돌 고르기
        top_r, top_c = top_pos[c]

        new_graph = deepcopy(graph)
        new_top_pos = deepcopy(top_pos)

        attack_range = new_graph[top_r][top_c]
        queue = deque()
        queue.append((top_r, top_c, attack_range))
        new_graph[top_r][top_c] = 0
        brick_cnt = 1
        

        while queue:
            row, col, n = queue.popleft()
            # 상하좌우, 사정거리 내 벽돌 터지기
            # new_graph[row][col] = 0  # 터트리기
            # brick_cnt += 1

            for i in range(4):
                for area in range(1, n):
                    nr = row + (dr[i] * area)
                    nc = col + (dc[i] * area)
                    if nr < 0 or nc < 0 or nr >= H or nc >= W:
                        break
                    if new_graph[nr][nc] == 0:
                        continue

                    # attack_range = new_graph[row][col]
                    attack_range = new_graph[nr][nc]  # [fix] nr로 써야됐음
                    queue.append((nr, nc, attack_range))
                    new_graph[nr][nc] = 0
                    brick_cnt += 1

        # # 벽돌 내리기
        for down_c in range(W):
            stack = []
            for r in range(H - 1, -1, -1):
                if new_graph[r][down_c] != 0:
                    stack.append(new_graph[r][down_c])
                    new_top_pos[down_c] = (H-len(stack), down_c)  # 높은 위치 갱신


            stack_length = len(stack)
            if stack_length == 0:
                new_top_pos[down_c] = -1

            for r in range(H):
                if r >= H-stack_length:
                    new_graph[r][down_c] = stack.pop()
                else:
                    new_graph[r][down_c] = 0


        answer = max(answer, cnt+brick_cnt)

        dfs(new_graph, cnt + brick_cnt, depth + 1, new_top_pos)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(H)]

    # top_li = []
    # top_li 도 전달해야 한다
    # top_pos = defaultdict(tuple)
    top_pos = [-1 for _ in range(W)]
    total_brick = 0
    for c in range(W):
        for r in range(H):
            if graph[r][c] != 0:
                top_pos[c] = (r, c)
                total_brick += H-r
                break
    # print(top_pos)
    # break
    # pprint(top_pos)
    answer = 0
    dfs(graph, 0, 0, top_pos)  # 현재 그래프, 깨진 벽돌 수, depth
    # print(total_brick, answer)
    answer = total_brick - answer

    print(f'#{tc} {answer}')
    # break