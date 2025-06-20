from itertools import permutations

def check(c, d, e, f, stack):
    if c >= 1:
        for x in range(c):
            stack.append('+')
    if d >= 1:
        for x in range(d):
            stack.append('-')
    if e >= 1:
        for x in range(e):
            stack.append('*')
    if f >= 1:
        for x in range(f):
            stack.append('/')
    return stack

def cal(a, b, c):
    if c == '+':
        return a + b
    if c == '-':
        return a - b
    if c == '*':
        return a * b
    if c == '/':
        if a < 0:
            return -(-a // b)
        else:
            return a // b

def check2():
    for y in range(len(co)):
        sum = a[0]  
        for x in range(0, len(a) - 1):
            sum = cal(sum, a[x + 1], co[y][x])
        li.append(sum)

k = 0  
n = int(input())
a = list(map(int, input().split()))
c, d, e, f = map(int, input().split())
stack = []
co = []
li = []
check(c, d, e, f, stack)

for x in set(permutations(stack, len(stack))):
    co.append(x)

check2()

print(max(li))
print(min(li))
