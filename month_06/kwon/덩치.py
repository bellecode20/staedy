# boj 7568 S5
n = int(input())
 
data = [] 
ans = [] 
for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b)) 
 
for i in range(n):
    cnt = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]: # 몸무게와 키 모두 자신보다 큰 사람의 수 count
            cnt += 1 
    ans.append(cnt + 1) 
 
for d in ans:
    print(d,end=" ")
