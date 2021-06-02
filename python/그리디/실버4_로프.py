# 나의 풀이
from itertools import combinations

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

combi = []
result = []
lst.sort(reverse=True)
for i in range(1, n+1):
    value = 0
    combi = list(combinations(lst, i))[:1]
    # print(combi)
    value = min(combi[0]) * i
    result.append(value)

result.sort(reverse=True)
print(result[0])


# 남의 풀이
n = int(input())
rope = []
result = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)

for i in range(n):
    result.append(rope[i]*(i+1))

print(max(result))