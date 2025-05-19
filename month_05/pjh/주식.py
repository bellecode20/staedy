T = int(input())
for tc in range(1,T+1):
    N = int(input())
    stocks = list(map(int,input().split()))
    s_cnt = 0
    s_price = 0
    sell = 0
    ans = 0 
    # 계속 감소하는 경우 0, 계속 증가하는 경우 마지막에 다팔기
    if stocks == sorted(stocks,reverse=True):
        print(0)
    elif stocks == sorted(stocks):
        for i in range(N-1):
                sell += stocks[i]
        print((stocks[N-1]*(N-1)) - sell)
    else:
        max_v = max(stocks)
        for i in range(N):
            if stocks[i] < max_v:
                s_cnt += 1
                s_price += stocks[i]
            elif stocks[i] == max_v:
                ans += stocks[i]*s_cnt - s_price
                if i == N-1:
                     continue
                max_v = max(stocks[i+1:])
                s_cnt = 0
                s_price = 0
        print(ans)