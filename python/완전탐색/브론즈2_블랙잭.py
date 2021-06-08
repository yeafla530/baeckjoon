n, m = map(int, input().split())
number = list(map(int, input().split()))

max_value = 0
min_sub_value = 987654321
result = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for z in range(j+1, n):
            max_value = number[i] + number[j] + number[z]
            # print(max_value, number[i], number[j], number[z])
            if min_sub_value > m - max_value and max_value <= m:
                min_sub_value = m - max_value
                result = max_value
                # print(result)
                

print(result)
