n, k = map(int, raw_input().split(' '))

yy = map(int, raw_input().split(' '))

#print n, k
l = 0

xx = range(1, n+1)
xy = []

for i in yy:
	indx = (l + i) % len(xx)
	xy.append(xx[indx])
	del xx[indx]
	l = indx % len(xx)

for x in xy:
	print x,