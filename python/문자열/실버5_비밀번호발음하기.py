# 모음 하나를 반드시 포함
# 모음 3개 혹은 자음 3개 연속으로 오면 안됨(2개까지허용)
# 같은 글자 연속으로 2번오면 안되지만 ee와 oo는 가능

word = ''
vowel = ['a', 'e', 'i', 'o', 'u']
while word != 'end':
    word = input()
    if word == 'end':
        break
    v_check = False
    three_check = True
    ctn_check = True

    before = word[0]
    vo_count = 1 # 모음 count
    co_count = 1 # 자음 count
    if before in vowel:
        v_check = True
    for i in range(1, len(word)):
        # 모음 하나를 반드시 포함
        if word[i] in vowel:
            v_check = True

        # 모음 3개 혹은 자음 3개 연속으로 오면 안됨(2개까지허용)
        if (before in vowel and word[i] in vowel):
            vo_count += 1
            if vo_count >= 3:
                three_check = False
        elif (before not in vowel and word[i] not in vowel):
            co_count += 1
            if co_count >= 3:
                three_check = False
        else:
            vo_count = 1
            co_count = 1
            before = word[i]

        # 같은 글자 연속으로 2번오면 안되지만 ee와 oo는 가능
        print(before, word[i])
        if before == word[i] and (before != 'e' or before != 'o'):
            ctn_check = False

    print(v_check, three_check, ctn_check)
    if v_check and three_check and ctn_check:
        print("<{}> is acceptable.".format(word))
    else:
        print("<{}> is not acceptable.".format(word))