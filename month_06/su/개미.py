# [BOJ] 개미 https://www.acmicpc.net/problem/3048

import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 파일이 있는 디렉토리를 기준으로 작업 디렉토리 설정
os.chdir(current_dir)
sys.stdin = open('input.txt', "r")

a_len, b_len = map(int, input().split())
a = list(input())
b = list(input())
T = int(input())
ants = a[::-1] + b
jump = 0

# 개미를 한 줄로 본다.
# 방향이 다른 개미를 만나면 swap하고, idx를 바꿔준다.

a_len, b_len = len(a), len(b)
N = len(ants)
dir = [-1] * a_len + [1] * b_len

for t in range(T):
    idx = 0
    while idx < N - 1:
        if dir[idx] == -1 and dir[idx + 1] == 1:  # 반대 방향인 경우
            ants[idx], ants[idx + 1] = ants[idx + 1], ants[idx]  # swap
            dir[idx], dir[idx + 1] = dir[idx + 1], dir[idx]  # swap
            idx += 2
        else:
            idx += 1

    

print("".join(ants))