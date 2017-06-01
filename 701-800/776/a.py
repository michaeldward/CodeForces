l1 = raw_input().split(' ')

x = int(raw_input())

n1 = l1[0]
n2 = l1[1]

for i in range (0, x):
	print n1, n2
	l2 = raw_input().split(' ')
	if n1 == l2[0]:
		n1 = l2[1]
	elif n2 == l2[0]:
		n2 = l2[1]
print n1, n2