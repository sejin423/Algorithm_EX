# n과 m을 공백으로 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문    
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우. 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드 미방문시
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] == 1
        # 상,하,좌,우 재귀적으로 호출하여 처리
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 위치에 대하여 음료 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현 위치에서 dfs 수행
        if dfs(i,j) == True:
            result += 1

print(result)      
