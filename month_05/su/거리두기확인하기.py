# https://school.programmers.co.kr/learn/courses/30/lessons/81302

# # 대기실 5개, 크기는 5 * 5
# # 응시자 간 거리는 맨허튼 거리 2이하 불가
# #     다만 파티션 있는 경우는 맨허튼 거리 관계없음

from collections import deque

def solution(places):
    answer = []
    
    def is_safe(place):
        grid = [list(row) for row in place]  # 2D 리스트로 변환
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 네 방향
        
        for i in range(5):
            for j in range(5):
                if grid[i][j] == "P":
                    queue = deque([(i, j, 0)])  # 시작 위치와 거리(0) 추가
                    visited = [[False] * 5 for _ in range(5)]
                    visited[i][j] = True
                    
                    # BFS로 거리두기 검사
                    while queue:
                        r, c, d = queue.popleft()
                        
                        if d > 0 and grid[r][c] == "P":
                            # 시작 위치 외에 다른 'P'를 발견한 경우 거리두기 위반
                            return False
                        
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                                if grid[nr][nc] == "X":
                                    continue  # 칸막이는 탐색 중지
                                if d < 2:  # 거리가 2 이내인 경우에만 탐색
                                    visited[nr][nc] = True
                                    queue.append((nr, nc, d + 1))
        
        return True
    
    for place in places:
        if is_safe(place):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer
