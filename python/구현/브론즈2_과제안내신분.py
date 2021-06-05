import sys
input = sys.stdin.readline

attendance = [0] * 31

for _ in range(28):
    n = int(input())
    attendance[n] = 1

index_lst = []

# enumerate사용시 index, value사용가능
index_lst = [i for i, value in enumerate(attendance) if value == 0]
index_lst.remove(0)
index_lst.sort()

for num in index_lst:
    print(num)

if index_lst[0] > index_lst[1]:
    max_num = index_lst[0]
    min_num = index_lst[1]
else:
    max_num = index_lst[1]
    min_num = index_lst[0]

print(min_num)
print(max_num)