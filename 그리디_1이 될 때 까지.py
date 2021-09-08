# 첫째 줄에 N(2<= N <=100,000)과 K(2<= K <=100,000)가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다

#단순풀이
# N과 K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

#n이 k 이상이라면 k로 나누기
while n >= k:
    # n이 k로 나누어 떨어지지 않는다면 n에서 1 뺴기
    while n % k != 0:
        n -= 1
        result += 1
    # k 로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 구하기
while n > 1:
    n -= 1
    result += 1

print(result)

#-----------------------------------------------
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n -1)
print(result)
