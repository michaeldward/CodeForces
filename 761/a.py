x = map(int, raw_input().split(' '))

a = x[0]

b = x[1]

if (a == b == 0):
	print "NO"
elif (a == b) or (a == b + 1) or (b == a + 1):
	print "YES"
else:
	print "NO"