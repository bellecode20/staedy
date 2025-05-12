N = int(input())

dp = [1]*10

for i in range(2,N+1):
    for j in range(10):
        dp[j] = sum(dp[j:])

ans = sum(dp)
print(ans%10007)