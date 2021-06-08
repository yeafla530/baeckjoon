a, b, c, d, e, f = map(int, input().split())

result = []
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            result = [x, y]
            break

for i in range(2):
    print(result[i], end=' ')

# 가감법
a, b, c, d, e, f = map(int, input().split())
x = (c*e-b*f)//(a*e-b*d)
y = (c*d-a*f)//(b*d-a*e)
print(x, y)