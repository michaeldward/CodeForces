xx = map(int, raw_input().split(' '))
yy = map(int, raw_input().split(' '))

a = xx[0]
b = xx[1]

c = yy[0]
d = yy[1]

aa = []
done = False

for x in range(0, 2000):
	aa.append(b + (x * a))

for x in range(0, 2000):
	y = d + (x * c)
	if y in aa:
		print y
		done = True
		break
if not done:
	print -1