t = int(input()) # T
for _ in range(t): # 입력반복
    string = input() # 입력 string값
    dic = dict()
    for i in range(len(string)): # string단어 개수 count
        if string[i] == ' ':
            continue
        if string[i] in dic:
            dic[string[i]] += 1
        else:
            dic[string[i]] = 1
        
    max_value = 0 # count한 value값 중 최대값 찾기 
    for value in dic.values():
        if max_value < value:
            max_value = value
    
    count = 0 # 최대값 2개이상인지 확인
    result = '' # 출력값
    for key, value in dic.items():
        print(key, value)
        if value == max_value:
            count += 1
            result = key
    if count == 1:
        print(result)
    else:
        print('?')
            