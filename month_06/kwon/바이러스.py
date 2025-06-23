# boj 2606 S3

def dfs(arr, x):
    global cnt 
    visited[x] =1 
    for i in arr[x]:
        if visited[i] == 0:
            cnt += 1
            dfs(arr, i)

n = int(input())
pairs = int(input())
computers = [[] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(pairs):
    s, e = map(int, input().split())
    computers[s].append(e)
    computers[e].append(s)

dfs(computers, 1)

print(cnt) 