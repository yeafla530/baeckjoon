n = int(input())
count = 0
for _ in range(n):
    word = input()
    lst = [word[0]] # word check할 list
    before = word[0] # 그 전 문자
    flag = True # 그룹단어인지 아닌지 체크
    for i in range(1, len(word)):
        if before != word[i]:
            if word[i] in lst:
                flag = False
                break
            lst.append(word[i])
            before = word[i] 
    
    if flag:
        count += 1
    
print(count)
