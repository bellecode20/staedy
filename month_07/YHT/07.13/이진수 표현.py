C = int(input())
for _ in range(C):
    N, M = map(int, input().split())
    mask = (1 << N) - 1
    if (M & mask) == mask:
        print("ON")
    else:
        print("OFF")