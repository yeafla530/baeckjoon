n = int(input())

result = 987654321
sum_value = 0
for m in range(n, 1, -1):
    sum_value = m
    for j in range(len(str(m))):
        sum_value += int(str(m)[j])
    
    if sum_value == n and m < result:
        result = m

    
if result == 987654321:
    print(0)
else:
    print(result)