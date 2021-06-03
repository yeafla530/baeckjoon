# i,  j n//2 가운데부터 시작 
# i 는 1증가, j는 고정
# j는 1증가, i는 고정
# i는 2증가, j는 고정
# j는 2증가, i는 고정
# i는 3증가, j는 고정
# j는 3증가, i는 고정

n = int(input())
target = int(input())
snail = [[0] * n for _ in range(n)] # 초기화

# 중간값부터 시작
a = n // 2 
b = n // 2


count = 0 # 홀수인지 짝수인지 판별 (2번 진행해야 i, j +, -가 바뀜)
go = 1 # 해당 방향으로 몇칸씩 나갈것인지 
num = 1 # snail에 1씩 증가하게될 수
result = '' # 좌표

snail[a][b] = num # 초기화

while num != n*n:
    
    count += 1 # 몇번 진행했는지 1씩 증가

    if count % 2 != 0: # 홀수번진행(i움직임)
        if go % 2 != 0: # 홀수칸만큼 나아감
            for i in range(go):
                a -= 1
                num += 1
                snail[a][b] = num
                if num == n*n:
                    break
                
        else: # 짝수칸만큼 나아감
            for i in range(go):
                a += 1
                num += 1
                snail[a][b] = num
                if num == n*n:
                    break
                    
    else:  # 짝수번 진행(j움직임)
        if go % 2 != 0: # 홀수칸만큼 나아감
            for i in range(go):
                b += 1
                num += 1
                snail[a][b] = num
                if num == n*n:
                    break
            go += 1
            
        else: # 짝수칸만큼 나아감
            for i in range(go):
                b -= 1
                num += 1
                snail[a][b] = num
                if num == n*n:
                    break
            go += 1  

for i in range(n):
    for j in range(n):
        print(snail[i][j], end=' ')
        if snail[i][j] == target:
            result += str(i+1) + ' ' + str(j+1)
    print(end='\n')

print(result)

