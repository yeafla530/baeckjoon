from collections import deque

def bfs(computer, i, visited):
    queue = deque([i])
    while queue:
        for i in computer[queue.pop()]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
        

n = int(input())
link = int(input())
answer = 0
visited = [0] * (n+1)
computer = [[] for _ in range(n+1)]
for i in range(link):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

bfs(computer, 1, visited)
print(sum(visited)-1)