# [PGR] https://school.programmers.co.kr/learn/courses/30/lessons/340212

def solution(diffs, times, limit):
    answer = int(1e9)
    N = len(diffs)
    limit -= sum(times)
    
    Flag = False
    start, end = 1, max(diffs)
    
    
    while start <= end:
        mid = (start + end) // 2
        cur_time = 0
        for i in range(N):
            if diffs[i] > mid:
                gap = diffs[i] - mid
                # if i == 0:
                #     cur_time += gap 
                cur_time += gap * (times[i-1] + times[i])
                            
        if cur_time == limit:
            answer = mid
            return answer
        elif cur_time < limit:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1
        
        # level += 1
        
    return answer