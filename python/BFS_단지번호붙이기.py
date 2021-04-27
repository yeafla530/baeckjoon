from collections import deque

N = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, cnt, x, y):
    graph[x][y] = 0
    queue = deque([(x,y)])
    # print(queue)
    while len(queue) != 0:
        x, y = queue.popleft()
        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0<= ny < N:
                if graph[nx][ny] == 1:
                    cnt += 1
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
    return cnt
graph = [list(map(int, input())) for _ in range(N)]

cnt = 0
answer = []

for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            answer.append(bfs(graph, cnt+1, i, j))

print(len(answer))
for i in sorted(answer):
    print(i)