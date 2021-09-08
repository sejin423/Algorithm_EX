"""
N,M이 주어진다. M은 입력으로 주어지는 연산의 개수
M개의 줄에는 각각의 연산이 주어진다
'팀 합치기' 연산은 0, a, b 형태로 주어진다. 이는 a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미
'같은 팀 여부 확인' 연산은 1, a, b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속해 있는 지를 확인하는 연산이다
a,b는 N 이하의 양의 정수이다
'같은 팀 여부 확인' 연산에 대하여 한줄에 하나씩 yes 혹은 no로 결과를 출력한다
"""

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, b)
    b = find_parent(parent, a)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# n,m 입력받기
n, m = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (n + 1)

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(0, n + 1):
    parent[i] = i

# 각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, input().split())
    # 합집합 연산인 경우
    if oper == 0:
        union_parent(parent, a, b)
    # 찾기 연산인 경우
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
