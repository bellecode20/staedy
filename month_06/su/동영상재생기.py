# [PGR] https://school.programmers.co.kr/learn/courses/30/lessons/340213

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''

    def to_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"  # f-string으로 자리수 맞춰 줄 수 있다.

    def to_seconds(str_time):
        minutes, seconds = map(int, str_time.split(":"))  # map으로 리스트 내 모든 원소를 int로 변환 가능
        return minutes * 60 + seconds


    video_sec = to_seconds(video_len)
    pos_sec = to_seconds(pos)
    op_start_sec, op_end_sec = to_seconds(op_start), to_seconds(op_end)
    
    for cmd in commands: 
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
        if cmd == "next": 
            pos_sec = min(video_sec, pos_sec + 10)
        elif cmd == "prev": 
            pos_sec = max(0, pos_sec - 10)
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    answer = to_time(pos_sec)
    
    return answer