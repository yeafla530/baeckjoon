# 최소를 찾는 문제 = bfs
# 나의 풀이
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

from collections import deque

def bfs(miro, visited, n, m, x, y, result):
    global dx, dy
    # print(visited)
    visited[y][x] = 1
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == m and ny == n and visited[ny][nx] < result:
                visited[ny][nx] = visited[y][x] + 1
                return visited[ny][nx]
            if 0 <= nx <= m and 0 <= ny <= n:
                if visited[ny][nx] == 0 and miro[ny][nx] == 1:
                    # print(ny, nx)
                    queue.append((nx, ny))
                    visited[ny][nx] = visited[y][x] + 1
    # return result



n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
n, m = n-1, m-1
result = 987654321
# print(visited)
print(bfs(miro, visited, n, m, 0, 0, result))


# 다른 사람풀이
from sys import stdin
from collections import deque

n, m = map(int, input().split())
matrix = [stdin.readline().strip() for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited[0][0] = 1
queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()
    if x == n-1 and y == m-1:
        print(visited[x][y])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = x + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[nx][ny] + 1
                queue.append((nx, ny))
