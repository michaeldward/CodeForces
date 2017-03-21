x = map(int, raw_input().split(' '))

a = x[0]

b = x[1]

y = 0

while (a <= b):
	a = a * 3
	b = b * 2
	y = y + 1

print y