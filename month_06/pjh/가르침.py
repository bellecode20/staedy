from itertools import combinations
N, K = map(int,input().split())
word = [list(input()) for _ in range(N)]
# k는 5이상이어야 최소한 1개라도 읽을 수 있음 'a','c','i','n','t'
anta = ['a','c','i','n','t']
l_word = [[] for _ in range(N)]      # 더 배워야 하는 글자 리스트
max_cnt = 0
plus = set()
if K<5:
    print(0)
    exit()
can_learn = []
for i in range(N):
    l_word[i] = list(set(word[i][4:-4])-set(anta))

for w in l_word:    
    if len(w)>K-5:
        continue
    can_learn.append(w)    
    plus.update(w)
plus = list(plus)
if not plus or len(plus)<=K-5:
    print(len(can_learn))
    exit()
for comb in combinations(plus,K-5):
    cnt = 0
    comb_set = frozenset(comb)  # 해시값 미리 계산
    cnt = sum(1 for w in can_learn if set(w) <= comb_set)
    max_cnt = max(cnt,max_cnt)
print(max_cnt)