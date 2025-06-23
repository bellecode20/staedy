
'''
이거 걍 combination 구해서 최대 길이 구하면 되는거 아닌가?

'''
from itertools import combinations
T=int(input())
for i in range(1,T+1):
    
    q2=[]
    N=int(input())
    a=list(map(int,input().split()))
    for y in range(1,len(a)+1):
        for x in combinations(a,y):
            q=0
            for z in range(len(x)-1):
                if(x[z]<x[z+1]):
                    q+=1
            if(q==len(x)-1):
                q2.append(len(x))
    print(max(q2))