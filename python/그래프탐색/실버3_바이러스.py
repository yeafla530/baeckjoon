# 가까운 연결되어있는 것들 찾는 문제 = bfs
from collections import deque 

def bfs(computers, v, visited):
    queue = deque([v])
    visited[v] = 1
    while queue:
        for i in computers[queue.popleft()]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                
n = int(input())
line = int(input())
computers = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(line):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a) 

# print(computers)
bfs(computers, 1, visited)
print(sum(visited) - 1)