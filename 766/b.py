x = raw_input()

xx = map(int, raw_input().split(' '))


def compare(a, b, c):
	#print a, b, c
	if (a + b <= c):
		return False
	if (b + c <= a):
		return False
	if (a + c <= b):
		return False
	return True


def test():
	a = 0
	b = 1
	c = 2
	d = len(xx) - 1
	print a, b, c, d
	while (a <= d - 2 and b <= d - 1 and c <= d):
		print("tried")
		#print xx[a], xx[b], xx[c]
		if (compare(xx[a], xx[b], xx[c])):
			print "YO"
			return True
		if (c < d):
			c = c + 1
		elif (b < c):
			b = b + 1
		else:
			a = a + 1
	return False

y = test()

if y:
	print "YES"
else:
	print "NO"