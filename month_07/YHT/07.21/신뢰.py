T=int(input())
for i in range(1,T+1):
    a=list(map(str,input().split()))
    b=int(a[0])
    a.pop(0)
    B,O=[1,1],[1,1]
    t=0
    for x in range(0, 2*b, 2): 
        pos = int(a[x+1])
        if a[x]=='B':
            if B[0]<=pos<=B[1]:
                t+=1
                B[0]=B[1]=pos
                O[0]+=1
                O[1]+=1
            else:
                move = abs(pos - B[1])
                t += move + 1
                B[0] = B[1] = pos
                O[0] -= move + 1
                O[1] += move + 1
        if a[x]=='O':
            if O[0]<=pos<=O[1]:
                t+=1
                O[0]=O[1]=pos
                B[0]+=1
                B[1]+=1
            else:
                move = abs(pos - O[1])
                t += move + 1
                O[0] = O[1] = pos
                B[0] -= move + 1
                B[1] += move + 1
    print(f"#{i} {t}")
### 테케는 다맞는데 제출을 자꾸 틀림