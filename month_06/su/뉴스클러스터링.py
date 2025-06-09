# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/17677

from collections import defaultdict
def solution(str1, str2): 
    def getBigram(s):
        bigrams = defaultdict(int)
        for i in range(len(s) - 1):
            new_str = s[i:i+2]
            if new_str.isalpha():
                bigrams[new_str.lower()] += 1 # 특수문자가 포함되지 않은 경우에만 카운팅한다.
        return bigrams

    bigram_1 = getBigram(str1)
    bigram_2 = getBigram(str2)
    obj_total = defaultdict(int, {**bigram_1, **bigram_2})
    
    intersectionCount = 0 
    unionCount = 0
    for key in obj_total.keys():
        thisIntersection = min(bigram_1[key], bigram_2[key]) 
        unionCount += obj_total[key] - thisIntersection # 합집합
        intersectionCount += thisIntersection # 교집합
        
    print(intersectionCount, unionCount)
    # return;
        
    if intersectionCount == 0 or unionCount == 0:
        J = 1 # A와 B가 공집합인 경우
        return;
    else:
        J = intersectionCount / unionCount
    
    return int(J * 65536)