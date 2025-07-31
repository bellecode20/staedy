def dfs(x,y):
    global count
    visit[x][y]=1
    count+=1
    for dir in range(4):
        nx=x+dx[dir]
        ny=y+dy[dir]
        if(0<=nx<N and 0<=ny<M and visit[nx][ny]==-1 and a[nx][ny]==1):
            count+=1
            dfs(nx,ny)
    return count
T=int(input())
dx=[0,0,-1,1]
dy=[-1,1,0,0]
for i in range(1,T+1):
    M,N,K=map(int,input().split())
    a=[[0]*M for _ in range(N)]
    for x in range(K):
        V,C=map(int,input().split())
        a[C][V]=1
    visit=[[-1]*M for _ in range(N)]
    
    q=[]
    count=0
    for x in range(N):
        for y in range(M):
            if(a[x][y]==1 and visit[x][y]==-1):
                count=dfs(x,y)
                q.append(count)
    print(len(q))