# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18GHd6IskCFAZN
T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    s = input()

    suffixes = sorted(s[i:] for i in range(len(s)))
    if 1 <= K <= len(suffixes):
        ans = suffixes[K - 1]  
    else:
        "none"
    print(f"#{tc} {ans}")
