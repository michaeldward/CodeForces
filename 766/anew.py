a = raw_input()
b = raw_input()

if a != b: #strings are different
	if sorted(a) == sorted(b):
		print -1
	else:
		print max(len(a), len(b))
elif a == b:
	print -1

