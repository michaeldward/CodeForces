aa = map(int, raw_input().split(' '))
bb = map(int, raw_input().split(' '))
cc = map(int, raw_input().split(' '))


n = aa[0]

l = aa[1]


def array_contains(a, b):
	return any(a == b[i:len(a)+i] for i in xrange(len(b) - len(a)+1))

xx = []
yy = []
#print len(cc)
#print cc[len(cc) - 1]
#print (cc[len(cc) - 1] - cc[0]) 
#print (bb[len(bb) - 1] - bb[0])
#if (cc[len(cc) - 1] - cc[0]) == (bb[len(bb) - 1] - bb[0]):
for x in range(0, len(cc) - 1):
	xx.append(cc[x+1] - cc[x])
	yy.append(bb[x+1] - bb[x])
xx.append((l - cc[len(cc) - 1]) + cc[0])
yy.append((l - bb[len(bb) - 1]) + bb[0])
zz = xx + xx
#print zz
#print yy
if array_contains(yy, zz):
	print "YES"
else:
	print "NO"