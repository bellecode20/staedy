from collections import deque
def bfs(sr,sc,horse):
    q = deque()
    q.append((sr,sc,horse))
    visited[horse][sr][sc] = 1
    while q:
        r,c,h = q.popleft()
        if h < K:
            for dir in range(8):
                nr = r+hr[dir]
                nc = c + hc[dir]
                if nr < 0 or nr >= H or nc < 0 or nc >= W or monkey[nr][nc] > 0 or visited[h+1][nr][nc] > 0:
                    continue
                visited[h+1][nr][nc] = visited[h][r][c] + 1
                q.append((nr,nc,h+1))
            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]
                if nr < 0  or nr >= H or nc < 0 or nc >= W or monkey[nr][nc] > 0 or visited[h][nr][nc] > 0:
                    continue
                visited[h][nr][nc] = visited[h][r][c] + 1
                q.append((nr,nc,h))
        else:
            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]
                if nr < 0  or nr >= H or nc < 0 or nc >= W or monkey[nr][nc] > 0 or visited[h][nr][nc] > 0:
                    continue
                visited[h][nr][nc] = visited[h][r][c] + 1
                q.append((nr,nc,K))

    

               



K = int(input())
W , H = map(int,input().split())
monkey = [list(map(int,input().split())) for _ in range(H)]
hr = [-2,-2,-1,1,-1,1,2,2]
hc = [-1,1,-2,-2,2,2,-1,1]
dr = [-1,1,0,0]
dc = [0,0,-1,1]

visited = [[[0]*W for _ in range(H)] for _ in range(K+1)]

bfs(0,0,0)
min_v = float('inf')
for k in range(K+1):
    if visited[k][H-1][W-1] > 0 and min_v > visited[k][H-1][W-1]:
        min_v = visited[k][H-1][W-1]

if min_v < 50000:
    print(min_v-1)
else:
    print(-1)