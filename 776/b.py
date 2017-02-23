def primes_sieve(x):
	b = False
	a = [True] * x
	a[0] = a[1] = False
	for(i, isprime) in enumerate(a):
		if isprime:
			for n in xrange(i*i, x, i):
				a[n] = False
				b = True
	if b:
		print 2
	else:
		print 1
	for i in range(2, x):
		if a[i] == True:
			print 1,
		else:
			print 2,


y = int(raw_input())
primes_sieve(y+2)
