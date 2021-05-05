from collections import deque


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited_dfs):
    visited_dfs[v] = 1
    print(v, end=' ')
    for i in sorted(graph[v]):
        if visited_dfs[i] == 0:
            dfs(graph, i, visited_dfs)

def bfs(graph, v, visited_bfs):
    queue = deque([v])
    visited_bfs[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if visited_bfs[i] == 0:
                visited_bfs[i] = 1
                queue.append(i)


dfs(graph, v, visited_dfs)
print('')
bfs(graph, v, visited_bfs)
