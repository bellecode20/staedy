T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    scores_order = sorted(scores)
    idx_high = 0
    ans = 1
    for i in range(1,N):
        if scores_order[i][1] < scores_order[idx_high][1]:
            idx_high = i
            ans += 1
    
    print(ans)
