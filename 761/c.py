xx = map(int, raw_input().split(' '))

n = xx[0]

m = xx[1]

yy = []


def password_check(ss):
	sa = "123456789"
	sb = "abcdefghijklmnopqrstuvwxyz"
	sc = "#*&"
	saa = False
	sbb = False
	scc = False

	for x in ss:
		if x in sa:
			saa = True
		if x in sb:
			sbb = True
		if x in sc:
			scc = True
	return (saa and sbb and scc)


for x in range(0, n):
	xb = raw_input()
	yy.append(xb)

for x in yy:
	print password_check(x)


