#https://school.programmers.co.kr/learn/courses/30/lessons/389479
def solution(players, m, k):
    answer = 0
    active = 0
    expire = [0] * (24 + k + 1)

    for i in range(24):
        active -= expire[i]
        required = players[i] // m 

        if active < required:
            need = required - active
            answer += need
            active += need
            expire[i + k] += need

    return answer
