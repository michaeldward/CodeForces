vowels = "aeiouyAEIOUY"

ccu = "BCDFGHJKLMNPQRSTVWXZ"

ccl = "bcdfghjklmnpqrstvwxz"

xx = raw_input()

xy = []

for x in xx:
	if (vowels.find(x) == -1):
		u = ccu.find(x)
		l = ccl.find(x)
		if (u != -1):
			xy.append('.')
			xy.append(ccl[u])
		else:
			xy.append('.')
			xy.append(x)
print ''.join(xy)