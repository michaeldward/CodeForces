xx = map(int, raw_input().split(' '))

n = xx[0]
m = xx[1]
a = xx[2]


b = n / a
if (n % a > 0):
	b = b + 1

c = m / a
if (m % a > 0):
	c = c + 1

print (b * c)