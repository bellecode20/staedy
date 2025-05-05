from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx, sy = i, j
            graph[i][j] = 0
            break

size = 2        
eaten = 0
time_spent = 0 
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
while True:
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    dist[sx][sy] = 0
    q.append((sx, sy))

    candidates = []
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1 and graph[nx][ny] <= size:
                dist[nx][ny] = dist[x][y] + 1
                if 0 < graph[nx][ny] < size:
                    candidates.append((dist[nx][ny], nx, ny))
                q.append((nx, ny))

    if not candidates:
        break
    candidates.sort()
    d, nx, ny = candidates[0]

    time_spent += d
    eaten += 1
    graph[nx][ny] = 0  
        
    if eaten == size:
        size += 1
        eaten = 0

    sx, sy = nx, ny  

print(time_spent)

