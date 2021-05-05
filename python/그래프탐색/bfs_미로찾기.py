from sys import stdin
from collections import deque

n, m = map(int, input().split())
matrix = [stdin.readline().strip() for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit[0][0] = 1
queue = deque([(0,0)])

while queue:
    x, y = queue.popleft()
    if x == n-1 and y == m-1:
        print(visit[x][y])
        break
    # print(x)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i] 
        
        if 0 <= nx < n and 0 <= ny < m:
            if visit[nx][ny] == 0 and matrix[nx][ny] == '1':
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
