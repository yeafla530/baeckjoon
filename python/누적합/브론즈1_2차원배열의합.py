# n, m = map(int, input().split())
# lst = [list(map(int, input().split())) for _ in range(n)]

# k = int(input())
# for _ in range(k):
#     i, j, x, y = map(int, input().split())
#     count = 0
#     for a in range(i-1, x):
#         for b in range(j-1, y):
#             count += lst[a][b]

#     print(count)

# 누적합 풀이
n, m = map(int, input().split())
lst = []
dp = [[0]*(m+1) for _ in range(n+1)]
for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        # 사방의 값을합친 것
        print(lst[i-1][j-1], dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        dp[i][j] = lst[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1]-dp[i-1][y]+dp[i-1][j-1])