from collections import deque
def bfs(si,sj):
    q = deque()
    vv = [[0]*5 for _ in range(5)]

    q.append((si,sj))
    vv[si][sj] = 1
    cnt = 1

    while q:
        ci,cj = q.popleft()
        for dir in range(4):
            ni = ci + di[dir]
            nj = cj + dj[dir]
            if ni < 0 or ni >=5 or nj < 0 or nj >= 5 or visited[ni][nj] != 1 or vv[ni][nj] == 1:
                continue
            q.append((ni,nj))
            vv[ni][nj] = 1
            cnt += 1
    return cnt == 7

def check():
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1:
                return bfs(i,j)


def dfs(n,cnt,scnt):
    global ans
    if cnt > 7:
        return
    if n ==25:
        if cnt == 7 and scnt >= 4:
            if check():
                ans += 1
        return
    visited[n//5][n%5] = 1
    dfs(n+1,cnt+1,scnt+int(girls[n//5][n%5]=='S'))
    visited[n//5][n%5] = 0
    dfs(n+1,cnt,scnt)
di = [-1,1,0,0]
dj = [0,0,-1,1]
girls = [input() for _ in range(5)]
ans = 0
visited = [[0]*5 for _ in range(5)]
dfs(0,0,0)
print(ans)