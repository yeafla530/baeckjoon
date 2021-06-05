n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=' ')
    for i in sorted(graph[v]):
        if visited[i] == 0:
            dfs(graph, i, visited) 

from collections import deque
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
        


dfs(graph, 1, visited_dfs)
print()
bfs(graph, 1, visited_bfs)
