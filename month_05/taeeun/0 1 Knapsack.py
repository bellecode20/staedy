# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBJAVpqrzQDFAWr


def knapsack(N, K, objects):
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        volume, value   = objects[i - 1]

        for w in range(K + 1):
            if volume > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - volume] + value)

    return dp[N][K]

T = int(input())
for tc in range(1, T + 1):
    ans = 0
    N, K = map(int, input().split())
    objects = [0] * N

    for i in range(N):
        vc = tuple(map(int, input().split()))
        objects[i] = vc

    ans = knapsack(N, K, objects)
    print(f'#{tc} {ans}')