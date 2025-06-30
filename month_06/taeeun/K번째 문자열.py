# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18KWf6ItECFAZN
T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    s = input()
    n = len(s)

    subs = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            subs.add(s[i:j])

    sorted_subs = sorted(subs)
    if 1 <= K <= len(sorted_subs):
        ans = sorted_subs[K - 1]  
    else:
        ans ="none"
    print(f"#{tc} {ans}")