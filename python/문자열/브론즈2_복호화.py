t = int(input())
for _ in range(t):
    string = input()
    dic = dict()
    for i in range(len(string)):
        if string[i] == ' ':
            continue
        if string[i] in dic:
            dic[string[i]] += 1
        else:
            dic[string[i]] = 1
        

    max_value = 0
    for value in dic.values():
        if max_value < value:
            max_value = value
    
    count = 0
    result = ''

    for key, value in dic.items():
        print(key, value)
        if value == max_value:
            count += 1
            result = key

    if count == 1:
        print(result)
    else:
        print('?')
            