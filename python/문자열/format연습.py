print('Format example. {{}}, {}'.format('test'))
# Format example.{}, test

print('This is value {{{0}}}'.format(1212))
# This is value {1212}

print('this is {0:<10} | done {1:<5} |'.format('left', 'a'))

print('this is {0:>10} | done {1:>5} |'.format('right', 'b'))

print('this is {0:^10} | done {1:^5} |'.format('center', 'c'))

print('this is {0:-<10} | done {1:o<5} |'.format('left', 'a'))
print('this is {0:+>10} | done {1:0>5} |'.format('right', 'b'))
print('this is {0:.^10} | done {1:@^5} |'.format('center', 'c'))

print('정수 3자리 : {0:03d}, {1:03d}'.format(12345, 12))
print('아래 2자리 : {0:0.2f}, 아래 5자리 : {1:0.5f}'.format(123.12345667, 3.14))

for a in range(2, 4):
	for b in range(3, 6):
		print('{0} x {1} = {2:2}'.format(a, b, a*b))

'''