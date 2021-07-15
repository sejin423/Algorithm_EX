# 커리큘럼
"""
동빈이가 듣고자 하는 강의의 수 N이 주어진다
N개의 줄에는 각 강의의 강의 시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 자연수로 주어지며, 각 자연수는 공백으로 구분한다. 이때 강의 시간은 100,000 이하의 자연수이다
강의 번호는 1부터 N 까지로 구성되며, 각 줄은 -1로 끝난ㄴ다
N개의 강의에 대하여 수강하기 까지 걸리는 최소 시간을 한줄에 하나씩 출력
"""
from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[0] for i in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))   
    # 첫 번쨰 수는 시간 정보를 담고있음
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
        
# 위상 정렬 함수
def topology_sort():
    # 알고리즘 수행 결과를 담을 리스트
    result = copy.deepcopy(time)
    # 큐 기능을 위한 deque 라이브러리 사용
    q = deque()
    # 처음 시작할 떄는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
            
    # 큐가 빌때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1            
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v + 1):
        print(result[i])

topology_sort()
