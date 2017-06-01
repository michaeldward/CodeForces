xx = raw_input()

val = 0
c = 0
dang = False

for x in xx:
	if (x == val):
		c = c + 1
	else:
		val = x
		c = 1
	if (c > 6):
		dang = True

if (dang):
	print "YES"
else:
	print "NO"