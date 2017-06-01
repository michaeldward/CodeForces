x = raw_input()
y = map(int, raw_input().split(' '))

mn = abs(y[0] - y[1])
y.sort()
mnct = 0
#mnindx = []

#print y
for i in xrange(1, len(y)):
	a = abs(y[i] - y[i-1])
	if (a < mn) and (a > 0):
		mn = a
		mnct = 1
	elif (a == mn):
		mnct = mnct + 1
		#mnindx.append(i)

print mn, mnct