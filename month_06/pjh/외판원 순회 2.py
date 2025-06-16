def dfs(cnt,start,cost):
    global min_v
    global v
    # print(start)
    if cnt == N and W[start][v] > 0:
        cost += W[start][v]
        # print(cost)
        if min_v >= cost:
            min_v = cost
        return 
    # if cost >= min_v:
    #     return
    for i in range(N):
        if not visited[i] and W[start][i]>0:
            visited[i] = 1
            dfs(cnt+1,i,cost+W[start][i])
            visited[i] = 0
    
N = int(input())
W = [list(map(int,input().split())) for _ in range(N)]
min_v = float('inf')
for v in range(N):
    visited = [0]*N
    visited[v] = 1
    dfs(1,v,0)

print(min_v)