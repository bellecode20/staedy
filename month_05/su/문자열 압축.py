# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    # 예외 처리: 문자열 길이가 1인 경우
    if len(s) == 1:
        return 1

    min_length = len(s)  # 최소 길이를 s의 길이로 초기화

    def compress(unit):
        compressed = ""
        prev = s[:unit] # 첫번째 단위 문자열
        count = 1
        for i in range(unit, len(s), unit):
            if prev == s[i:i+unit]:
                count += 1
            else:
                if count == 1:
                    compressed += prev
                else:
                    compressed += (str(count) + prev)
                    
                count = 1
                prev = s[i:i+unit]
                
        # 남아있는 문자열 처리
        if count == 1:
            compressed += prev
        else:
            compressed += (str(count) + prev)
        return len(compressed)
    
    for i in range(1, (len(s) // 2) + 1):
        min_length = min(min_length, compress(i))
    
    return min_length