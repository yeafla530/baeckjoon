N = int(input())
time = [[0]*2 for _ in range(N)]


for i in range(N):
    k, v = map(int, input().split())
    time[i][0] = k
    time[i][1] = v

time.sort(key=lambda x: (x[1], x[0]))
print(time)
