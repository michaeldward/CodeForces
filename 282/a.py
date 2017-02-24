x = int(raw_input())

c = 0

for i in range(0, x):
	xy = raw_input()
	if xy.find('+') != -1:
		c = c + 1
	elif xy.find('-') != -1:
		c = c - 1

print c