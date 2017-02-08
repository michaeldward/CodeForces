x = raw_input()

xx = map(int, raw_input().split(' '))


def compare(a, b, c):
	#print a, b, c
	if (a + b < c):
		return False
	if (b + c < a):
		return False
	if (a + c < b):
		return False
	return True


def test():
	a = 0
	b = 1
	c = 2
	d = len(xx) - 1
	while (a < d - 2 or b < d - 1 or c < d):
		#print xx[a], xx[b], xx[c]
		if (compare(xx[a], xx[b], xx[c])):
			#print "YO"
			return True
		if (c < d):
			c = c + 1
		elif (b < d - 1):
			b = b + 1
		else:
			a = a + 1
	return False

y = test()

if y:
	print "YES"
else:
	print "NO"