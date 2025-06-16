# [BOJ] 연산자끼워넣기 https://www.acmicpc.net/problem/14888

import os
import sys

# 현재 파일이 있는 디렉토리를 기준으로 작업 디렉토리 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
sys.stdin = open('input.txt', "r")

# 식의 계산은 앞에서부터 진행한다.
# 나눗셈은 몫만 취한다.
# 음수를 양수로 나눌 때? 양수로 바꾼뒤 몫을 취하고, 그 몫을 음수로 바꾸기

# 심화 방식:dp를 적용할 수도 있다. 같은 연산자, 같은 갯수 사용한 경우 최대/최소 비교해서 미리 종료. 가지치기 할 수 있음

N = int(input())  
nums = list(map(int, input().split())) 
cals = list(map(int, input().split()))  # 연산자 총 갯수


dp_max = [0] * 4
dp_min = [0] * 4
min_answer = int(1e9)
max_answer = int(1e9) * -1

def dfs(result, depth, used_cals, cals_sequence):
    global min_answer, max_answer
    if depth == N:
        if min_answer > result:
            min_answer = result
        if max_answer < result:
            max_answer = result

    for i in range(4):
        new_used_cals = used_cals[:]
        if new_used_cals[i] == 0:  # 다 사용한 경우
            continue

        new_used_cals[i] -= 1
        if i == 0: 
            dfs(result + nums[depth], depth + 1, new_used_cals, cals_sequence + "+ ")
        elif i == 1:
            dfs(result - nums[depth], depth + 1, new_used_cals, cals_sequence + "- ")
        elif i == 2:
            dfs(result * nums[depth], depth + 1, new_used_cals, cals_sequence + "* ")
        else:
            new_result = result
            if result < 0:
                new_result = ((result * -1) // nums[depth]) * -1
            else:
                new_result = result // nums[depth]
            dfs(new_result, depth + 1, new_used_cals, cals_sequence + "% ")

dfs(nums[0], 1, cals, "")

print(max_answer)
print(min_answer)
