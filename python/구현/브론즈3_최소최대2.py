n = int(input())

for _ in range(n):
    push_num = int(input())
    lst = list(map(int, input().split()))
    min_n = min(lst)
    max_n = max(lst)
    print(str(min_n) + ' ' + str(max_n))


n = int(input())

for _ in range(n):
    push_num = int(input())
    lst = list(map(int, input().split()))
    min_n = 987654321
    max_n = -987654321 # 주의 : 최소값 -1,000,000까지있음
    for num in lst:
        if num < min_n:
            min_n = num
        if num > max_n:
            max_n = num
    
    print(str(min_n) + ' ' + str(max_n))