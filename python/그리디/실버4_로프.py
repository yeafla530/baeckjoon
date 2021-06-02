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