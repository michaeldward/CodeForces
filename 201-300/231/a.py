x = int(raw_input())

c = 0

for i in range(0, x):
	xx = map(int, raw_input().split(' '))
	xy = xx[0] + xx[1] + xx[2]
	if (xy > 1):
		c = c + 1

print c