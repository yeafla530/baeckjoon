poliomino = list(input().split('.'))
# print(poliomino)
a = 'AAAA'
b = 'BB'

result = ''
print(poliomino)

for i in range(len(poliomino)):
    x_len = len(poliomino[i]) 
    if x_len % 2 == 1:
        result = -1
        break
    if x_len // 4 != 0:
        result += a * (x_len // 4)
        x_len -= (x_len // 4) * 4
    
    if x_len // 2 != 0:
        result += b * (x_len // 2)
        x_len -= (x_len // 2) * 2
    
    if i != len(poliomino) -1 :
        result += '.'
    

print(result)



# 다른 사람 풀이
board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)

else:
    print(board)