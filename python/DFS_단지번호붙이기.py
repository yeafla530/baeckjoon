# 지도를 입력하여 단지수 출력하고
# 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력

def dfs(graph, cnt, x, y):
    graph[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 1:
                cnt = dfs(graph, cnt+1, nx, ny)

    return cnt
    


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
answer = []



for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            answer.append(dfs(graph, 1, i, j))
        
print(len(answer))
for i in sorted(answer):
    print(i)