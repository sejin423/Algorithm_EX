n = 1250 # 거슬러 주어야 하는 돈
count = 0
# 큰 단위의 돈부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n # 해당 화폐로 거슬러 줄 수 있는 동전의 개수
    n %= coin

print(count)
