N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))


memo = {}
def max_joy(sejun, i):
    if i == N:
        return 0
    if (i, sejun) in memo:
        return memo[(i, sejun)]
    
    # 선택 안 함
    res = max_joy(sejun, i+1)
    
    # 선택 함
    if sejun - L[i] > 0:
        res = max(res, J[i] + max_joy(sejun - L[i], i+1))
    
    memo[(i, sejun)] = res
    return res

ans = max_joy(100, 0)



print(ans)