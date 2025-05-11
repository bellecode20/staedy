from itertools import combinations

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    adj = [[0]*(N+1) for _ in range(N+1)]
    cnt = 0
    for k in range(M):
        x, y = map(int,input().split())
        adj[x][y] = 1
        adj[y][x] = 1


    for comb in combinations(range(1,N+1),3):    
        x,y,z = comb
        if adj[x][y] == 1 and adj[y][z] == 1 and adj[x][z]==1:
            cnt += 1
    print(f'#{tc} {cnt}')






