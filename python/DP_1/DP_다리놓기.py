for tc in range(int(input())):
    n,m = map(int, input().split())

    d = [[0]*31 for _ in range(31)]

    for i in range(1, n+1):
        d[i][i] = 1 
        for j in range(1, m+1):
            if i == 1:
                d[i][j] = j
            else:
                d[i][j] = d[i-1][j-1] + d[i][j-1]

    print(d[n][m]) 