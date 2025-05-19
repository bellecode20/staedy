
from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    INF = int(1e9)
    answer = [INF, INF] # [산봉우리 번호, intensity 최솟값]
    # paths = [[i지점, j지점, 시간]]
    
    gate_set = set(gates)
    summit_set = set(summits)
    info = defaultdict(list)
    for i, j, w in paths:
        info[i].append((j, w))
        info[j].append((i, w))
        
    def bfs():
        # cur_summits = set(summits)  # 집합으로 변경하여 빠른 조회
        # cur_summits = summits[:]
        intensity_list = [INF] * (n + 1) # 지금까지의 최대거리 기록하기
        hq = []
        
        for gate in gate_set:
            intensity_list[gate] = 0
            heapq.heappush(hq, (0, gate))
        
        while hq:
            current_intensity, node = heapq.heappop(hq)
            
            if node in summit_set:
                continue
            
            #### intensity가 더 크면 스킵해야 했다.
            if current_intensity > intensity_list[node]:
                continue
            
            for next_node, next_cost in info[node]:
                    
                ### 출입구가 아닌 경우에만 탐색!!!!
                new_intensity = max(next_cost, current_intensity)
                
                if new_intensity < intensity_list[next_node] and next_node not in gate_set:
                    intensity_list[next_node] = new_intensity
                    heapq.heappush(hq, (new_intensity, next_node))
        
        return intensity_list
                    
    intensity_list = bfs()
    # print("intensity_list", intensity_list)
    
    summits.sort()
    for summit in summits:
        top_num, max_intensity = answer # 더 낮은 intensity를 찾은 경우 갱신한다.
        if intensity_list[summit] < max_intensity:
            answer = [summit, intensity_list[summit]]
    return answer