https://www.acmicpc.net/problem/2870

import heapq

N = int(input())

ans = []

for i in range(N):
    x = input()
    l = len(x)
    is_num = False
    part = ''
    for j in range(l):
        if x[j].isdigit():
            is_num = True
            part += x[j]
        else:
            is_num = False
            if part != '':
                heapq.heappush(ans, int(part))
                part = ''
        if j == l-1 and part != '':
            heapq.heappush(ans, int(part))
            part = ''

while ans:
    print(heapq.heappop(ans))
        
        
       
