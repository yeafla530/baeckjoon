n=int(input())
tmp=list(map(int, input().split()))
mysum=[]
mysum.append(tmp[0]) #첫번째 수 넣기
ans=0
for i in range(1,n): # 이전값이랑 다음값 더함
    mysum.append(mysum[i-1]+tmp[i])

for i in range(n): # 정답에 
    # print(tmp[i], mysum[n-1], mysum[i], mysum[n-1]-mysum[i])
    ans+=tmp[i]*(mysum[n-1]-mysum[i])
print(ans)