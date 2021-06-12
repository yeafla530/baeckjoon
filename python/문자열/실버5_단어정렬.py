n = int(input())
words = set()
for _ in range(n):
    word = input()
    words.add((len(word), word))
    
words = list(words)
# 길이가 짧은 것부터
# 길이가 같으면 사전순으로
words.sort(key = lambda x : (x[0], x[1])) # 알아두기

for w in words:
    print(w[1])