x = raw_input()

y = map(int, raw_input().split(' '))

q = max(y)



y = filter(lambda a: a != q, y)


if(len(y) > 0):
	b = min(y)
	y = filter(lambda a: a != b, y)

print len(y)