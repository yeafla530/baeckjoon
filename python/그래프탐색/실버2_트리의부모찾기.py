# 부모에 있는 자식들을 구하는 것은 bfs

from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
parent[1] = -1
while queue:
    v = queue.popleft()
    # print(graph[v])
    for i in graph[v]:
        if parent[i] == 0:
            queue.append(i)
            parent[i] = v 

# print(parent[2:])
for i in parent[2:]:
    print(i)
