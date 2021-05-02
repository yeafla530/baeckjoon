# n = int(input())

# if n % 2 == 0:
#     print('CY')
# else:
#     print("SK")

n = int(input())

d = [0] * 1001
# 상근 1 창영 0
d[1] = 1
d[2] = 0
d[3] = 1
d[4] = 0

for i in range(5, n+1):
    # i가 5면 상근이가 이김 (선빵이 이김)
    if d[i-1] == 0 and d[i-3] == 0:
        d[i] = 1 
    else:
        d[i] = 0

if d[n] == 1:
    print('SK')
else:
    print('CY')