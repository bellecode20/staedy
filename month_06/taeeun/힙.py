import heapq

for tc in range(1, int(input()) + 1):
    n = int(input())                             
    heap = []
    res  = []

    for _ in range(n):
        op, *rest = map(int, input().split())
        if op == 1:                               
            heapq.heappush(heap, -rest[0])   
        else:                                         
            res.append(-heapq.heappop(heap) if heap else -1)
    print(f"#{tc}", *res)
