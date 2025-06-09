for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())   # 두 집합 크기

    A = set()
    while len(A) < n:                 
        A.update(input().split())

    cnt = 0
    read = 0
    while read < m:              
        tokens = input().split()
        read += len(tokens)
        for s in tokens:
            if s in A:
                cnt += 1

    print(f"#{tc} {cnt}")
