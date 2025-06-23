# 백준 14888 연산자 끼워넣기

N = int(input())

A_list = list(map(int, input().split()))

plus, minus, multiply, divide = list(map(int, input().split()))


max_ans = -10**9  # 최소값은 -10억
min_ans = 10**9  # 최대값은 10억

def dfs(idx, current, plus, minus, multiply, divide):
    global max_ans, min_ans
    if idx == N:
        max_ans = max(max_ans, current)
        min_ans = min(min_ans, current)
        return

    nxt = A_list[idx]
    if plus > 0:
        dfs(idx+1, current + nxt, plus-1, minus, multiply, divide)
    if minus > 0:
        dfs(idx+1, current - nxt, plus, minus-1, multiply, divide)
    if multiply > 0:
        dfs(idx+1, current * nxt, plus, minus, multiply-1, divide)
    if divide > 0:
        # 문제에서 정의된 C++14 방식 나눗셈 구현
        if current < 0:
            dfs(idx+1, - (abs(current) // nxt), plus, minus, multiply, divide-1)
        else:
            dfs(idx+1, current // nxt, plus, minus, multiply, divide-1) 

dfs(1, A_list[0], plus, minus, multiply, divide)

print(max_ans)
print(min_ans)