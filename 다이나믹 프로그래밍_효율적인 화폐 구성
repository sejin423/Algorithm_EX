# n m 이 주어진다
# 이후 n개의 줄에는 각 화폐의 가치가 주어진다. 화폐가치는 10,000보다 작거나 같은 자연수이다
# m원을 만들기 위한 최소한의 화폐개수를 출력한다
# 불가능 할떄에는 -1을 출력

# 정수 n, m 입력받기
n, m = map(int, input().split())

# n개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))
# 한번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍_보텀업
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        # (i - k)원을 만드는 방법이 존재하는 경우
        if d[j - array[i]] != 10001:
            d[j] = d[j - array[i] + 1]

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
