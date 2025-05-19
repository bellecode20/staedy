from collections import deque
T = 10
for tc in range(1,T+1):
    V, E = map(int,input().split())
    work = list(map(int, input().split()))
    list_work = [0]*(V+1)
    list_order = [[] for _ in range(V+1)]
    ans = []
    q = deque()
    for i in range(E):
        p , l = work[2*i], work[2*i+1]
        list_work[l] += 1
        list_order[p].append(l)
    for i in range(1,V+1):
        if list_work[i] == 0:
            q.append(i)
    while q:
        p = q.popleft()
        if (list_work[p] == 0) and (p not in ans):
            ans.append(p)
        for i in range(len(list_order[p])):
            list_work[list_order[p][i]] -= 1
            if list_work[list_order[p][i]] == 0:
                q.append(list_order[p][i])
    print(f'#{tc}', *ans)