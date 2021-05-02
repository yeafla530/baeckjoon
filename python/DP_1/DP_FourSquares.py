import math

n = int(input())

d = [0] * (n+1)
d[1] = 1
d[2] = 2
d[3] = 3


print(d)
for i in range(4, n+1):
    s_num = math.sqrt(i)
    print(type(s_num))
    if type(s_num) == int:
        print('hellop', i)
