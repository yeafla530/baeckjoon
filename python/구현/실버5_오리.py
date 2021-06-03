sound = input()
duck = 'quack'

count = 0 # 오리울음개수
length = len(sound) # 소리 길이
n = 0 # length만큼 증가시킬 수
d = 0 # 오리 울음 위치


while n != length:
    d = d%5

    if duck[d] == sound[n]:
        if d % 5 == 0:
            count += 1
        d += 1
        n += 1
        
    else:
        n += 1

print(count) 
    