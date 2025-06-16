for tc in range(1, int(input()) + 1):
    a, b, k = map(int, input().split())
    s   = a + b                 # 전체 사탕 수(항상 일정)
    p2  = pow(2, k, s)          # 2^k mod s
    na  = (a * p2) % s          # k번 후 나연이 사탕
    ans = min(na, s - na)       # 더 적은 쪽의 사탕 개수
    print(f"#{tc} {ans}")