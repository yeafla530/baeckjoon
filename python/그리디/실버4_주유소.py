# 이동하는 최소 비용 계산
n = int(input())
length = list((map(int, input().split())))
cost = list((map(int, input().split())))

# 길이는 상관없고, 가격만 확인했을 때
# 해당 값이 최소 값이 아니면 다음목적지까지 가기위한 기름만 넣음
# 만약 해당값이 최소값이면 끝까지의 거리값 * 리터당가격 해줌
min_cost = min(cost[:len(cost)-1])
result = 0
flag = False
# print(min_cost)

for i in range(n-1):
    # print(length[i], cost[i])
    if cost[i] == min_cost:
        flag = True
        result += length[i] * min_cost
    else:
        if flag == False:
            result += length[i] * cost[i]
        else:
            result += length[i] * min_cost

print(result)

# 다른 풀이
# 지향하기 
n = int(input())
length = list((map(int, input().split())))
cost = list((map(int, input().split())))

result = 0
min_cost = 987654321

for i in range(n-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    result += min_cost * length[i]

print(result)