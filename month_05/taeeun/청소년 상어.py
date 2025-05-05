from collections import deque

dr = [-1, -1,  0, 1, 1, 1, 0, -1]
dc = [ 0, -1, -1, -1, 0, 1, 1,  1]

board=[[0]*4 for _ in range(4)]
dirs = [[0]*4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = data[2*j]
        dirs[i][j] = data[2*j+1] - 1

init = board[0][0]
init_dir = dirs[0][0]
board[0][0] = -1

ans = 0
q = deque()
q.append((board, dirs, 0, 0, init))

while q:
    g, d, sx, sy, total = q.popleft()
    ng = [row[:] for row in g]
    nd = [row[:] for row in d]

    for f in range(1, 17):
        found = False
        for x in range(4):
            for y in range(4):
                if ng[x][y] == f:
                    fr, fc = x, y
                    fd = nd[x][y]
                    found = True
                    break
            if found:
                break
        if not found:
            continue
        for i in range(8):
            ndir = (fd + i) % 8
            nx, ny = fr + dr[ndir], fc + dc[ndir]
            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == sx and ny == sy):
                ng[fr][fc], ng[nx][ny] = ng[nx][ny], ng[fr][fc]
                nd[fr][fc], nd[nx][ny] = nd[nx][ny], ndir
                break

    sdir = nd[sx][sy]
    moved = False
    for step in range(1, 4):
        nx, ny = sx + dr[sdir]*step, sy + dc[sdir]*step
        if not (0 <= nx < 4 and 0 <= ny < 4):
            break
        if ng[nx][ny] == 0:
            continue
        moved = True
        tg = [row[:] for row in ng]
        td = [row[:] for row in nd]
        eat = tg[nx][ny]
        tg[sx][sy] = 0
        tg[nx][ny] = -1
        q.append((tg, td, nx, ny, total + eat))
    if not moved:
        ans = max(ans, total)

print(ans)

