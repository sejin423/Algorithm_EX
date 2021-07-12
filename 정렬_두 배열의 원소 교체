# n k 가 공백으로 구분되어 입력된다
# 배열 A의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다
# 배열 B 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다
# 최대 k번의 바꿔치기 연산을 수행해 만들수 있는 배열 A의 모든 원소의 합의 최댓값을 출력

# n, k 입력받기
n, k = map(int, input().split())
# 배열 a 입력
a = list(map(int, input().split()))
# 배열 b 입력
b = list(map(int, input().split()))

a.sort() # 배열 A 오름차순 정렬
b.sort(reverse=True) # 배열 b 내림차순 정렬

# 첫 번째 인덱스 부터 확인하여, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은경우
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i] # 두 원소 교체
    # A의 원소가 B의 원소보다 클 경우 중지
    else:
        break

print(sum(a))
