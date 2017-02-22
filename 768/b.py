import math

z = map(int, raw_input().split(' '))

x = [z[0]]

d = False


q = int(math.log(z[0], 2))


#for i in range(0, (q/2) - 1):
#	x.append(1)
#	x.append(0)
#x.append()

while not d:
	d = True
	for a in range(0, q):
		if (x[a] > 1):
			d = False
			q = x[a]
			del x[a]
			x.insert(a, (q/2))
			x.insert(a, (q%2))
			x.insert(a, (q/2))
			a = a + 2

c = 0
print x
#for a in x:
#	if a is 1:
#		c = c + 1

#for a in range(z[1] - 1, z[2]):
#	if (x[a] == 1):
#		c = c + 1
#print c