from collections import deque
def bfs():
    q = deque()
    v = [[set() for _ in range(C)] for _ in range(R)]
    ans = 1

    q.append((0,0,arr[0][0]))
    v[0][0].add(arr[0][0])

    while q:
        ci,cj,cv = q.popleft()
        ans = max(ans, len(cv))
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<R and 0<=nj<C and arr[ni][nj] not in cv:
                if cv+arr[ni][nj] not in v[ni][nj]:
                    q.append((ni,nj,cv+arr[ni][nj]))
                    v[ni][nj].add((cv+arr[ni][nj]))
    return ans


R, C = map(int, input().split())
arr = list(input() for _ in range(R))

ans = bfs()
print(ans)