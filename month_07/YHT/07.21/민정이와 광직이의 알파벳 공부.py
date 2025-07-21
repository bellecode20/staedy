from itertools import combinations

T = int(input())
for i in range(1, T + 1):
    q = []
    N = int(input())
    for _ in range(N):
        a = input().strip()
        q.append(set(a))

    result = 0
    full = set('abcdefghijklmnopqrstuvwxyz')

    for y in range(1, len(q) + 1):
        for combo in combinations(q, y):
            letters = []
            for word in combo:
                for ch in word:
                    if ch not in letters:
                        letters.append(ch)
            if len(letters) == 26:
                result += 1

    print(f'#{i} {result}')
