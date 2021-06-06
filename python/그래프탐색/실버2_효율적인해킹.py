# def dfs(computers, v, count, visited, point):
#     visited[v] = 1
#     count[point] += 1
#     for i in computers[v]:
#         if visited[i] == 0:
#             # print(i, end=' ')
#             dfs(computers, i, count, visited, point)

from collections import deque
def bfs(computers, v, count, visited, point):
    queue = deque([v])
    count[point] += 1
    visited[v] = 1
    while queue:
        i = queue.popleft()
        for com in computers[i]:
            if visited[com] == 0:
                # print(com)
                queue.append(com)
                count[point] += 1
                visited[com] = 1

n, m = map(int, input().split())
computers = [[] for _ in range(n+1)]
count = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    computers[b].append(a)

# print(computers)

for i in range(1, n+1): # 1부터 시작
    point = i
    visited = [0] * (n+1)
    # dfs(computers, i, count, visited, point)
    bfs(computers, i, count, visited, point)
# print(count)

max_value = max(count)
result = [x for x, value in enumerate(count) if value == max_value]
print(*sorted(result))