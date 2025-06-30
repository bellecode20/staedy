# https://www.acmicpc.net/problem/21610
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
commands = [tuple(map(int, input().split())) for _ in range(M)]

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

dx = [0, 0, -1, -1, -1,  0, 1, 1, 1]
dy = [0, -1,-1,  0,  1,  1, 1, 0,-1]

for d, s in commands:
    moved = []
    for r, c in clouds:
        nr = (r + dx[d] * s) % N
        nc = (c + dy[d] * s) % N
        moved.append((nr, nc))
    
    visited = [[False]*N for _ in range(N)]
    for r, c in moved:
        grid[r][c] += 1
        visited[r][c] = True
    
    for r, c in moved:
        cnt = 0
        for i in (2, 4, 6, 8):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > 0:
                cnt += 1
        grid[r][c] += cnt
    
    clouds = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] >= 2:
                clouds.append((i, j))
                grid[i][j] -= 2

print(sum(map(sum, grid)))