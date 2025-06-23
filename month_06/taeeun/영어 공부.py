# swea 10507 영어공부
T = int(input())
for tc in range(1, T + 1):
    N, P = map(int, input().split())

    days = []
    while len(days) < N:
        days.extend(map(int, input().split()))

    last = max(days) 
    visited = [False] * (last + 1)
    for d in days:
        visited[d] = True


    left = right = 1           
    blanks_left = P         
    length      = 0           
    best        = P + 1   

    while right <= last:
        if visited[right]:
            length += 1
            right  += 1
        elif blanks_left:     
            blanks_left -= 1
            length      += 1
            right       += 1
        else:
            if not visited[left]:
                blanks_left += 1
            length -= 1
            left   += 1
            continue          

        best = max(best, length + blanks_left)

    print(f"#{tc} {best}")
