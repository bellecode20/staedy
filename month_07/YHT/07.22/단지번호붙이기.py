def dfs(x,y):
    global count
    visit[x][y]=1
    for dir in range(4):
        nx=dx[dir]+x
        ny=dy[dir]+y
        if 0<=nx<N and 0<=ny<N and visit[nx][ny]==-1 and a[nx][ny]==1:
            count+=1
            dfs(nx,ny)
    return count
N=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
dir=0
count=1
a=[list(map(int,input().strip())) for _ in range(N)]
visit=[[-1]*N for _ in range(N)]
result=[]
for x in range(N):
    for y in range(N):
        if(a[x][y]==1 and visit[x][y]==-1):
            count=(dfs(x,y))
            result.append(count)
            count=1
result.sort()
print(len(result))
for i in result:
    print(i)
    
    