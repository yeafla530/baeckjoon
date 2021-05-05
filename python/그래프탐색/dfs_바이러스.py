def dfs(computer, i, visited):
    global answer
    visited[i] = 1
    for a in computer[i]:
        if not visited[a]:
            answer += 1
            print(a, visited, computer)
            dfs(computer, a, visited)
    
# dfs시 주의 
# 인접행렬 방식을 사용할 때는 양쪽 인덱스에 값을 추가해줘야한다 
n = int(input())
link = int(input())
answer = 0
visited = [0] * (n+1)
computer = [[] for _ in range(n+1)]
for i in range(link):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

print(computer[1].pop())
dfs(computer, 1, visited)
print(answer)