# 정수 N이 주어진다
# 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고, 1,000,000 이하
# 정수 M이 주어진다
# 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000이하
# 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes, 아니면 no를 출력

# 이진 탐색 소스코드_반복문
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# n 입력
n = int(input())

# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 정렬 수행

# m 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int,input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('No', end=' ')

#------------------------------------------------------
# 계수 정렬 방식
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('No', end=' ')
        
# ------------------------------------------------------
# 집합 자료형 방식
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합 자료형에 기록
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('No', end=' ')
