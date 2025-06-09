import heapq
MOD = 20171109

for tc in range(1, int(input()) + 1):
    n, first = map(int, input().split())

    lower = [-first]  
    upper = []       
    acc   = 0

    for _ in range(n):
        a, b = map(int, input().split())
        for v in (a, b):
            if v <= -lower[0]:
                heapq.heappush(lower, -v)
            else:
                heapq.heappush(upper, v)

            if len(lower) < len(upper):
                heapq.heappush(lower, -heapq.heappop(upper))
            elif len(lower) > len(upper) + 1:
                heapq.heappush(upper, -heapq.heappop(lower))

        acc = (acc - lower[0]) % MOD  

    print(f"#{tc} {acc}")
