# 8진수 => 2진수
# 8진수 1개씩 끊어 2진수로 만들어주기
# ex ) 3 => 011, 1 => 001, 4 => 100

n = input() # 8진수
result = []
answer = ''

for num in n: # 수의 길이 333334가 최대,,,
    #print(num)
    for _ in range(3):
        result.append(str(int(num) % 2))
        num = int(num) // 2
    result = result[::-1]
    #print(result)
    answer += ''.join(result)
    result = []

print(int(answer))


print(bin(int(input(), 8))[2:])