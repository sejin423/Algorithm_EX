# 식량창고의 개수 n이 주어진다
# 공백으로 구분되어 각 식량창고에 저장된 식략의 개수 K가 주어진다
# 개미전사가 얻을 수 있는 식량의 최댓값 출력

# n 입력받기
n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행_보텀업
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i -2] + array[i])

print(d[n -1])
