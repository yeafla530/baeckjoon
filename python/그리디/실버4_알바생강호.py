# 강호가 받을 수 있는 팁의 최대값 
import sys
input = sys.stdin.readline

n = int(input())
tip = []
for _ in range(n):
    tip.append(int(input()))

# 팁은 돈 + 1 - 받은등수 라고 할수 있음

tip.sort(reverse=True)
max_coin = 0

for i in range(n):
    if tip[i] - i > 0:
        max_coin += tip[i] - i
    

print(max_coin)