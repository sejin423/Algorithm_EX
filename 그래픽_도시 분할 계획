# 도시 분할 계획
"""
집의 개수 N, 길의 개수 M이 주어진다. N은 2 이상 100,000 이하의 정수이고, M은 1이상 1,000,000 이하인 정수이다
M 줄에 걸쳐 길의 정보가 A, B, C 3개의 정수로 공백으로 구분되어 주어지는데 A번 집과 B번 집을 연결하는 길의 유지비가 C라는 뜻이다
첫째 줄에 길을 없애고 남은 유지비의 합의 최솟값을 출력한다
"""

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        b = parent[a]
    else:
        a = parent[b]
    
# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i
    
# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 하기 위해 튜플의 첫번쨰 원소를 비용으로 설정
    edges.append((cost, a, b))
    
# 간선을 비용순으로 정렬
edges.sort()
# 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선
last = 0

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
    
print(result - last)
