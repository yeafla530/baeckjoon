h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

start = h1*60*60+ m1*60 + s1
end = h2*60*60+ m2*60 + s2

print(start, end)

time = end - start if end > start else end - start + 24*60*60

h = time // 60 // 60
m = time // 60 % 60
s = time % 60
print("%02d:%02d:%02d" % (h, m, s))
