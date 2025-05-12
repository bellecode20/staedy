
directions = [(1,0), (0,1), (-1,0), (0, -1)]


def dfs(index, connected, wire_len):
    global best_cnt, ans



    remain = total_cores - index
    if connected + remain < best_cnt:
        return
    
    if connected + remain == best_cnt and wire_len >= ans:
        return

    if index == total_cores:
        if connected > best_cnt or (connected == best_cnt and wire_len < ans):
            best_cnt = connected
            ans = wire_len
        return
    

    cr, cc = core_coords[index]

    for dr, dc in directions:
        path = []
        nr, nc = cr + dr, cc + dc
        ok = True

        while 0 <= nr < N and 0 <= nc < N:
            if visited[nr][nc]:
                ok = False
                break
            path.append((nr, nc))
            if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
                break
            nr += dr
            nc += dc

        if not ok or (nr, nc) not in path:
            continue

        for pr, pc in path:
            visited[pr][pc] = True
        dfs(index + 1, connected + 1, wire_len + len(path))

        for pr, pc in path:
            visited[pr][pc] = False

    dfs(index + 1, connected, wire_len)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    core_coords = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                visited[i][j] = True
                if not(i == 0 or i == N-1 or j == 0 or j== N-1):
                    core_coords.append((i, j))

    best_cnt = 0
    ans = float('inf')

    total_cores = len(core_coords)
    dfs(0, 0, 0)


    print(f'#{tc} {ans}')

