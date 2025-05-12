from collections import deque

T = int(input())

directions = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (1,-1), (-1, 1), (-1, -1)]

def count_mines(r, c , N, matrix):
    count = 0
    for dir in directions:
        dr, dc = dir
        nr, nc = r + dr, c + dc
        if 0<= nr < N and 0 <= nc < N and matrix[nr][nc] == '*':
            count += 1
    return count

def bfs(r, c, N, matrix, visited):
    q = deque()
    q.append((r,c))
    visited[r][c] = True
    
    while q:
        cr, cc = q.popleft()
        for dir in directions:
            dr, dc = dir
            nr, nc = cr + dr, cc + dc
            if 0<= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if matrix[nr][nc] == '.':
                    visited[nr][nc] = True
                    if count_mines(nr, nc, N, matrix) == 0 :
                        q.append((nr,nc))



for tc in range(1, T+1):
    N = int(input())
    matrix = [input() for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    click_count = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '.' and not visited[i][j]:
                if count_mines(i, j, N, matrix) == 0:
                    bfs(i, j, N, matrix, visited)
                    click_count += 1

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '.' and not visited[i][j]:
                click_count += 1

    print(f'#{tc} {click_count}')

