def check(line, L):
    N = len(line)
    used = [False] * N 
    for i in range(N - 1):
        diff = line[i + 1] - line[i]

        if diff == 0:     
            continue
        if abs(diff) > 1:     
            return False

        if diff == -1:
            h = line[i + 1]
            for j in range(i + 1, i + 1 + L):
                if j >= N or line[j] != h or used[j]:
                    return False
                used[j] = True

        else:
            h = line[i]
            for j in range(i, i - L, -1):
                if j < 0 or line[j] != h or used[j]:
                    return False
                used[j] = True
    return True


N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for r in range(N):
    if check(grid[r], L):        
        cnt += 1
for c in range(N):
    if check([grid[r][c] for r in range(N)], L):  
        cnt += 1

print(cnt)