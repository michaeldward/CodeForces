aa = map(int, raw_input().split(' '))

bb = map(int, raw_input().split(' '))

x = aa[1]

c = 0

y = bb[x-1]

for i in bb:
	if (i >= y and i > 0):
		c = c + 1

print c