# 첫째 줄에 N(2<=N<=1,000), M(1<=M<=10,000), K(1<=K<=10,000)의 자연수가 주어지며 각 자연수는 공백으로 구분한다
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10,000이하의 수로 주어진다
# 입력으로 주어지는 K는 항상 M보다 작거나 같다

# n m k 의 값을 공백으로 구분하여 입력받기
n, m, k = map(int,input().split())

# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

# n개의 수 정렬
data.sort()
# 가장 큰 수
first = data[n-1]
# 두번쨰로 큰 수
second = data[n-2]

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k번 반복하여 더하기
        if m == 0:
            break
        result += first 
        m -= 1 # 횟수 1회 차감
    if m == 0: # 만일 m이 0 이라면 반복문 탈출
        break
    result += second # 두번째로 큰 수를 한번 더 더하기
    m -= 1 

# 최종 답안 출력
print(result)
##-----------------------------------------------------------##
# 3-2

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second
