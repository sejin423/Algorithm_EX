# 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M 이 공백을 기준으로 하여 각각 자연수로 주어진다 (1<=N, M<=100)
# 둘째 줄 부터 N 개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1이상 10,000 이하의 자연수이다

# min() 함수를 이용.
# n, m 을 공백을 이용해 입력받기
n, m = map(int, input().split())

result = 0
# 한줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data) # 현재 줄에서 가장 작은 값 찾기
    result = max(result, min_value) # 현재 줄에서 가장 큰 값 찾기
    
print(result)

#---------------------------------------------------------------------
# 2중 반목문 구조를 이용.

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    
    #가장 작은 수들 중에서 큰 수 찾기
    result = max(result, min_value)
    
print(result)
