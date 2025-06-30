# boj 20920 S3

n,m = map(int, input().split())
d = {}
for _ in range(n):
	name = input().strip()

	if len(name) < m:
		continue
	if d.get(name): # d.get()은 해당 값이 존재하면 값을 반환 없으면 None을 반환
		d[name][0] += 1
	else:
		d[name] = [1, len(name), name]
# 개수, 길이는 내림차순으로 단어는 사전순(오름차순)으로 정렬
ans = sorted(d.items(), key= lambda x: (-x[1][0], -x[1][1], x[1][2]))

for a in ans:
	print(a[0])