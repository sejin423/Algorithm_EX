# 도시의 개수 N, 통로의 개수 M, 메세지를 보내고자 하는 도시 C가 주어진다
# M + 1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다. 이는 특정도시 X에서 다른 특정도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미다
# 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.

import sys
import heapq

input = sys.stdin.readline
# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

# 노드의 개수, 간선의 개수, 시작 노드를 입력받기
n, m, start = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)
# 모든 간선 정보를 입력받기
for i in range(m):
    x, y, z = map(int, input().split())
    # X번 노드에서 Y번 노드로 가는 비용이 Z라는 의미
    graph[x].append((y, z))
    
# 다익스트라 알고리즘 구현
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0 이며 큐에 삽입
    heapq.heappush(q,(0, start))
    distance[start] = 0
    # 큐가 비어있지 않다면
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
        # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 도달 할 수 있는 노드의 개수
count = 0
# 도달 할 수 있는 노드 중에서 가장 멀리있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달 할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
        
# 시작 노드는 제외해야 함으로 count - 1 출력
print(count - 1, max_distance)
