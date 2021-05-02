n = int(input())

d = [0] * 1001
# 창영win 0, 상근win 1 
# 상근이가 유리 4개부터
# 1개일때 창영 win
d[1] = 0
# 2개일때 상근 win
d[2] = 1
# 3개일때 창영 win
d[3] = 0
# 1개일때 상근win 
# 상근이가 지는 경우가 있지만 상근이가 이기도록 설계가능 
d[4] = 1

for i in range(5, n+1):
    # 상근이가 이기는 경우를 캐치할 수 있음
    # 무조건 창영이가 이길 수 있도록 설계가능
    if d[i-1] and d[i-3] and d[i-4]:
        d[i] = 0
    else:
        d[i] = 1

if d[n] == 0:
    print("CY")
else:
    print("SK")


