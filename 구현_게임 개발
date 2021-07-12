# 첫째 줄에 맵의 세로크기 N과 가로크기 M을 공백으로 구분하여 입력한다. (3<= N, M <=50)
# 둘째 줄에 게임 캐릭터가 있는 칸의 좌표(A,B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다. 방향 d의 값으로는 다음과 같이 4가지가 존재한다. [0: 북, 1:동, 2:남 3: 서]
# 셋째 줄에 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 맵의 외각은 항상 바다이다.
# [0: 육지, 1: 바다]
# 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.

# n 와 m을 공백을 이용하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성해 0으로 초기화
d = [[0] * m for _ in range(n)]
# 캐릭터의 x, y 좌표와 방향을 입력받기
x, y, direction = map(int, input().split())
# 현재 방문 좌표 처리
d[x][y] = 1

# 맵 전체를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 위치 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
        # 회전한 이후에 정면에 가보지 않은 칸이 없거나 바다인 경우.
    else:
        turn_time += 1
    
    # 네 방향 모두 갈수 없을 경우.
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동.
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막힌 경우.
        else:
            break
        turn_time = 0
        
print(count)
