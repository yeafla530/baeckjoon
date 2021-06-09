arr = [[] for _ in range(15)]
for _ in range(5):
    string = input()
    for i in range(len(string)):
        arr[i].append(string[i])

result = ''

for i in range(len(arr)):
    result += ''.join(arr[i])
print(result)


# 다른 사람 풀이
text = []
for i in range(5):
    text.append(input())

for i in range(max(len(e) for e in text)): # text중 가장 긴 문자열만큼 
    for j in range(5):
        if i < len(text[j]): # 글자수체크(i) 보다 text[j] 길이가 짧으면 text[j]의 i번째가 없다는 뜻이므로
        # 건너뛰로 i보다 클때만 출력한다
            print(text[j][i], end='')
