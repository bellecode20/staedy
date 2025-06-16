# boj 2116

N = int(input()) # 주사위 개수 입력
dices = [list(map(int, input().split())) for _ in range(N)] # 주사위 정보 입력

dice_opposite = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0} # 주사위 마주보는 면

max_sum = 0

for i in range(6):
    sum = 0
    bottom = dices[0][i] # 첫 번째 주사위 아랫면
    top = dices[0][dice_opposite[i]] # 첫 번째 주사위 윗면

    # 옆 면의 최대 값 구하기
    side_numbers = []
    for j in range(6):
        if j != i and j != dice_opposite[i]:
            side_numbers.append(dices[0][j])
    side_max = max(side_numbers)
    sum += side_max

    for k in range(1, N):
        dice = dices[k]
        bottom_index = -1
        for idx in range(6):
            if dice[idx] == top:
                bottom_index = idx
                break
        top_index = dice_opposite[bottom_index]
        top = dice[top_index]
        side_numbers = []
        for j in range(6):
            if j !=  bottom_index and j != top_index:
                side_numbers.append(dice[j])
        side_max = max(side_numbers)
        sum += side_max
    max_sum = max(max_sum, sum)

print(max_sum)

# 주사위 개수 입력 받기
# 주사위 전개도 입력
# 마주 보는 주사위 구하기(AF(0,5)/BD(1,3)/CE(2,4))
# 아래 주사위의 윗면과 위 주사위의 아랫면의 숫자가 같아야 함
# 아래, 윗면의 숫자가 아닌 숫자 중에서 최대 구하기

