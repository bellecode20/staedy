def isqrt(n):
    lo, hi = 0, n
    while lo <= hi:
        mid = (lo + hi) // 2
        sq  = mid * mid
        if sq == n:
            return mid
        if sq < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

for tc in range(1, int(input()) + 1):
    n   = int(input())
    D   = 1 + 8 * n              # 판별식
    s   = isqrt(D)               # 정수 제곱근
    if s * s == D and (s - 1) % 2 == 0:
        k = (s - 1) // 2         # 정확히 삼각수인 단 수
    else:
        k = -1                   # 불가능
    print(f"#{tc} {k}")