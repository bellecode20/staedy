from collections import deque
def bfs(x,y):
    q=deque()
    visit[x][y]=1
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for dir in range(4):
            nx=x+dx[dir]
            ny=y+dy[dir]
            if(0<=nx<N and 0<=ny<M and a[nx][ny]==1 and visit[nx][ny]==0):
                visit[nx][ny]=visit[x][y]+1
                q.append((nx,ny))


N,M=map(int,input().split())
a=[list(map(int,input().strip())) for _ in range(N)]
visit=[[0]*M for _ in range(N)]
dx=[0,0,1,-1]
dy=[-1,1,0,0]
bfs(0,0)
print(visit[N-1][M-1])
