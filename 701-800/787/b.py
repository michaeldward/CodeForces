xx = map(int, raw_input().split(' '))

n = xx[0]
m = xx[1]

done = False

for x in xrange(0, m):
	yy = map(int, raw_input().split(' '))
	if (yy[0] == 0):
		continue
	if (yy[0] == 1):
		print "YES"
		done = True
		break
	else:
		z = {}
		d = False
		for y in xrange(1, len(yy)): #check for val and -val
			if (-yy[y]) in z:
				d = True
				break
			else:
				z[yy[y]] = True
		if not d:
			print "YES"
			done = True
			break
if not done:
	print "NO"