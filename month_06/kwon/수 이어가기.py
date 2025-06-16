# boj 2635 S5

N = int(input())
max_cnt = 0
answer = []

for second in range(1, N + 1):  # 두 번째 수를 1부터 N까지 시도
    seq = [N, second]
    while True:
        next_num = seq[-2] - seq[-1]
        if next_num < 0:
            break
        seq.append(next_num)

    if len(seq) > max_cnt:
        max_cnt = len(seq)
        answer = seq

print(max_cnt)
print(*answer)


