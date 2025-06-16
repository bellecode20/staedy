for tc in range(1, int(input()) + 1):
    n = int(input())
    names = {input() for _ in range(n)}        # 중복 제거
    ordered = sorted(names, key=lambda s: (len(s), s)) # 길이 사전순

    print(f"#{tc}")
    for name in ordered:
        print(name)