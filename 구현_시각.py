# 첫째 줄에 정수 N이 입력 (0<= N <=23)
# 00시 00분 00초부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

h = int(input())

count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 문자열 3이 포함되어있는지 확인하고 포함이 되어있으면 카운트.
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
