t = []
p = []
N = int(input())
for i in range(N):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

t = [0]+t
p = [0]+p
dp = [0]*(N+2)

# i + ti <= N

for i in range(1,N+1):
    dp[i] = max(dp[i-1],dp[i])
    if i + t[i] > N+1:
        continue
    dp[i+t[i]] = max(dp[i]+p[i],dp[i+t[i]])

    # else:
    #     dp[i+t[i]] = max(dp[i]+p[i],dp[i+t[i]])
print(max(dp))
