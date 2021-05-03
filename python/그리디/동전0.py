N, K = map(int, input().split())
coin = []

for _ in range(N):
    coin.append(int(input()))

result = 0 # 코인최소개수
coin.sort(reverse=True)

for i in coin:
    if i > K:
        continue
    if K == 0:
        break
    result += K//i
    K %= i

print(result)