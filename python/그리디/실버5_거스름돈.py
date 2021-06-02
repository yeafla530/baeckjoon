n = int(input())

count = 0 # 거스름돈 최소 개수
if n == 1 or n == 3:
    print(-1)
else:  
    count += n // 5
    n = n - (count * 5)

    if n % 2 != 0:
        count -= 1
        n += 5
        count += n // 2
        n = n - (count * 2)
    else:
        count += n // 2
        n = n - (count * 2)

    print(count)