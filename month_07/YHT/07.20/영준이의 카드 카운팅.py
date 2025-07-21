T=int(input())

for i in range(1,T+1):
    s=[0,'01','02','03','04','05','06','07','08','09','10','11','12','13']
    d=[0,'01','02','03','04','05','06','07','08','09','10','11','12','13']
    h=[0,'01','02','03','04','05','06','07','08','09','10','11','12','13']
    c=[0,'01','02','03','04','05','06','07','08','09','10','11','12','13']
    a=list(map(str,input().strip()))
    z=0
    print(f'#{i} ',end='')
    for x in range(len(a)):
        k=0
        if(a[x]=="S"):
            if(a[x+1]+a[x+2] in s):
                w=s.index(a[x+1]+a[x+2])
                s.pop(w)
            else:
                k=1
        if(a[x]=="H"):
            if(a[x+1]+a[x+2] in h):
                w=h.index(a[x+1]+a[x+2])
                h.pop(w)
            else:
                k=1
        if(a[x]=="C"):
            if(a[x+1]+a[x+2] in c):
                w=c.index(a[x+1]+a[x+2])
                c.pop(w)
            else:
                k=1
        if(a[x]=="D"):
            if(a[x+1]+a[x+2] in d):
                w=d.index(a[x+1]+a[x+2])
                d.pop(w)
            else:
                k=1
        if(k==1):
            print('ERROR')
            z=22
            break
    
    if(z!=22):
        print(len(s)-1,len(d)-1,len(h)-1,len(c)-1)