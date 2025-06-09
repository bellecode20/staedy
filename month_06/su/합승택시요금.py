# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/72413
# S -> N 시작점이 S, 도착점이 N인 경로
# N -> A 시작점이 N, 도착점이 A
# N -> B 시작점이 N, 도착점이 B

# S -> A 시작점이 S, 도착점이 B
# S -> B 시작점이 S, 도착점이 B

# 일단 시작점이 S고, 모든 도착점 구하기
from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    answer = 0
    INF = int(1e9)
    info = defaultdict(list)


    for c, d, f in fares:
        info[c].append((d, f))
        info[d].append((c, f))
    def dijkstra(start):
        distances = [INF] * (n + 1)
        # visited = [False] * (n + 1)

        pq = []
        distances[start] = 0
        heapq.heappush(pq, (0, start))
        while pq:
            dist, node = heapq.heappop(pq)
            # visited[node] = True
            if distances[node] < dist:
                continue
            for next_node, next_dist in info[node]:
                
                # if visited[next_node]:
                #     continue
                
                new_dist = min(next_dist + dist, distances[next_node])
                if new_dist < distances[next_node]:
                    distances[next_node] = new_dist
                    heapq.heappush(pq, (new_dist, next_node))
        return distances

    s_start_dist = dijkstra(s)
    a_start_dist = dijkstra(a)
    b_start_dist = dijkstra(b)
    min_cost = INF
    for i in range(1, n+1):
        min_cost =  min(s_start_dist[i] + a_start_dist[i] + b_start_dist[i], min_cost)
    
    return min_cost