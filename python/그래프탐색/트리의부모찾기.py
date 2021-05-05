from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
check = [0 for _ in range(n+1)]
answer = [0] * (n+1)
print(graph, check, answer)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모를 찾는 문제이므로 모든 자식을 탐색하는
# bfs를 쓰는게 좋음
queue = deque([1])

while queue:
    parent = queue.popleft()
    for a in graph[parent]:
        if check[a] == 0:
            answer[a] = parent
            queue.append(a)
            print(queue)
            check[a] = 1
            
for i in range(2, n+1):
    print(answer[i])
        