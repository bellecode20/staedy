# 백준 3190 뱀

from collections import deque

N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]         
for _ in range(K):                
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1                  

L = int(input())

turns = {}                                   
for _ in range(L):              
    t, d = input().split()
    turns[int(t)] = d


directions = [(-1,0), (0,1), (1,0), (0,-1)]

dir_idx = 1

snake = deque([(0, 0)])
body = {(0, 0)}

time = 0
while True:
    time += 1
    head_r, head_c = snake[0]
    nr, nc = head_r + directions[dir_idx][0], head_c + directions[dir_idx][1]

    if not (0 <= nr < N and 0 <= nc < N) or (nr, nc) in body:
        print(time)
        break

    snake.appendleft((nr, nc))
    body.add((nr, nc))

    if board[nr][nc] == 1:           # 사과가 있으면 먹고 길이 +1
        board[nr][nc] = 0
    else:                            # 없으면 꼬리 한 칸 줄이기
        tail = snake.pop()
        body.remove(tail)

    if time in turns:
        if turns[time] == 'L':       
            dir_idx = (dir_idx - 1) % 4
        else:                        
            dir_idx = (dir_idx + 1) % 4
