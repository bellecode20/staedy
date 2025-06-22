# boj 2578 S4

def check_bingo(arr):
    bingo = 0

    for i in range(5): # 가로
        if arr[i] == [0] * 5:
            bingo += 1
    
    for i in range(5): # 세로
        if [arr[j][i] for j in range(5)] == [0] * 5:
                bingo += 1

    if [arr[i][i] for i in range(5)] == [0] *5:
        bingo += 1

    if [arr[i][4-i] for i in range(5)] == [0] * 5:
        bingo += 1 

    return bingo 

chulsoo = [ list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
cnt = 0 
for i in range(5):
    for j in range(5):
        cnt += 1

        for k in range(5):
            for l in range(5):
                if mc[i][j] == chulsoo[k][l]:
                    chulsoo[k][l] = 0
                    
        if check_bingo(chulsoo) >= 3:
            print(cnt)
            exit()