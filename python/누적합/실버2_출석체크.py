n, k, q, m = map(int, input().split())
k_lst = list(map(int, input().split()))
q_lst = list(map(int, input().split()))
student = [a for a in range(3, n+3)]
visited = [0] * n

for a in q_lst:
    if a in k_lst:
        q_lst.remove(a)
print(q_lst)
for _ in range(m):
    s, e = map(int, input().split())
    count = set()
    for a in q_lst:
        print(a)
        for i in range(s-3, e-3):
            print(student[i])
            # 3, 5, 7의배수들 학생
            if student[i] in k_lst:
                count.add(student[i])
            else:
                if student[i] % a == 0:
                    visited[i] = 1
                    if student[i] in count:
                        count.remove(student[i])
                else:
                    count.add(student[i])

            print(count)
    print(len(count))
        